"""A test generator using Hypothesis ghostwriter."""

from hypothesis.extra import ghostwriter

from python_tool_competition_2024.generation_results import (
    FailureReason,
    TestGenerationFailure,
    TestGenerationResult,
    TestGenerationSuccess,
)
from python_tool_competition_2024.generators import FileInfo, TestGenerator


_NO_TESTABLE_FUNCTIONS_HEADER = "# Found no testable functions in"


class HypothesisGhostwriterTestGenerator(TestGenerator):
    """A test generator using Hypothesis ghostwriter."""

    def build_test(self, target_file_info: FileInfo) -> TestGenerationResult:
        """
        Genereate a test for the specific target file.

        Args:
            target_file: The `FileInfo` of the file to generate a test for.

        Returns:
            Either a `TestGenerationSuccess` if it was successful, or a
            `TestGenerationFailure` otherwise.
        """
        try:
            # with _add_to_sys_path(target_file_info.):
            test_body = _build_test_body(target_file_info)
        except ImportError as error:
            return TestGenerationFailure(
                ("The module could not be imported.", str(error)),
                FailureReason.UNEXPECTED_ERROR,
            )

        if test_body.startswith(_NO_TESTABLE_FUNCTIONS_HEADER):
            return TestGenerationFailure(
                ("Hypothesis Ghostwriter could not find any testable functions.",),
                FailureReason.NOTHING_GENERATED,
            )

        # replace common issue
        test_body = test_body.replace(
            "st.integers()", "st.integers(min_value=0, max_value=1_000)"
        )

        return TestGenerationSuccess(test_body)


def _build_test_body(target_file_info: FileInfo) -> str:
    return ghostwriter.magic(
        target_file_info.import_module(),
        # *_load_public_functions(target_file_info),
        style="pytest",
        annotate=True,
    )
