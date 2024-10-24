# Python Tool Competition Implementation Using Hypothesis ghostwriter

Uses the python-tool-competition-2024 to generate tests using the
Hypothesis ghostwriter. It is important to note that we have used Ghostwriter in a way is not (ideally) intended to (e.g., the ghostwriter often explicitly requires the user to provide some input), for a statement on how to use it for research prurposes, please refer to https://hypothesis.readthedocs.io/en/latest/ghostwriter.html#a-note-for-test-generation-researchers

For more information see
<https://github.com/ThunderKey/python-tool-competition-2024/>.

## Installation

* Install [poetry](https://python-poetry.org/)
* Run `poetry install`

## Development

The entry point called by `python-tool-competition-2024` is the `build_test`
method in `python_tool_competition_2024_hypothesis_ghostwriter/generator.py`.

## Calculating Metrics

Run `poetry run python-tool-competition-2024 run <generator name>`.

With `poetry run python-tool-competition-2024 run -h` you can find out what
generators were detected.
