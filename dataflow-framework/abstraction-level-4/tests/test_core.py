import pytest
from typing import Iterator, List

from ..core import apply_pipeline_stream
from ..adapter import adapt_processor
from ..processors.counter import LineCounter
from ..processors.joiner import LineJoiner
from ..processors.splitter import LineSplitter
from ..processors.filter import LineFilter

def to_uppercase(s: str) -> str:
    return s.upper()

def test_adapt_processor():

    adapter = adapt_processor(to_uppercase)
    input_lines = iter(["hello", "world"])
    result = list(adapter.process(input_lines))
    assert result == ["HELLO", "WORLD"]

def test_line_counter():

    counter = LineCounter({"format": "Line {count}: {line}"})
    input_lines = iter(["apple", "banana", "cherry"])
    result = list(counter.process(input_lines))
    assert result == [
        "Line 1: apple",
        "Line 2: banana",
        "Line 3: cherry"
    ]
    

    input_lines = iter(["date", "elderberry"])
    result = list(counter.process(input_lines))
    assert result == [
        "Line 4: date",
        "Line 5: elderberry"
    ]
    

    counter.reset()
    input_lines = iter(["fig"])
    result = list(counter.process(input_lines))
    assert result == ["Line 1: fig"]

def test_line_joiner():

    joiner = LineJoiner({"join_count": 2, "separator": " + "})
    input_lines = iter(["a", "b", "c", "d", "e"])
    result = list(joiner.process(input_lines))

    assert result == ["a + b", "c + d", "e"]
    

    joiner = LineJoiner({"join_count": 3, "separator": "-"})
    input_lines = iter(["1", "2", "3", "4", "5"])
    result = list(joiner.process(input_lines))
    assert result == ["1-2-3", "4-5"]

def test_line_splitter():

    splitter = LineSplitter({"delimiter": ","})
    input_lines = iter(["a,b,c", "d,e"])
    result = list(splitter.process(input_lines))
    assert result == ["a", "b", "c", "d", "e"]
    

    splitter = LineSplitter({"delimiter": ",", "max_splits": 1})
    input_lines = iter(["a,b,c", "d,e,f"])
    result = list(splitter.process(input_lines))
    assert result == ["a", "b,c", "d", "e,f"]

def test_line_filter():

    line_filter = LineFilter({"min_length": 3})
    input_lines = iter(["a", "ab", "abc", "abcd"])
    result = list(line_filter.process(input_lines))
    assert result == ["abc", "abcd"]
    

    line_filter = LineFilter({"contains": "b"})
    input_lines = iter(["apple", "banana", "cherry"])
    result = list(line_filter.process(input_lines))
    assert result == ["banana"]
    

    line_filter = LineFilter({"starts_with": "c"})
    input_lines = iter(["apple", "banana", "cherry"])
    result = list(line_filter.process(input_lines))
    assert result == ["cherry"]

def test_pipeline_integration():

    pipeline = [
        adapt_processor(lambda s: s.lower()),
        LineSplitter({"delimiter": ","}),
        LineCounter(),
        LineFilter({"min_length": 3}),
        adapt_processor(lambda s: s.upper())
    ]
    
    input_lines = iter(["A,BC,DEF", "GHI,J,KLM"])
    result = list(apply_pipeline_stream(input_lines, pipeline))
    
    expected = [
        "[1] A",
        "[3] DEF", 
        "[4] GHI",
        "[6] KLM"
    ]
    

    expected = [line.upper() for line in expected]
    assert result == expected
