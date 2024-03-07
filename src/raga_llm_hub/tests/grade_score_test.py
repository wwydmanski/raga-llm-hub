"""
Grade Score Test
"""

import textstat


def grade_score_test(prompt, response=None, threshold=5):
    """
    Provides the grade score. The grade score means the number of years of education generally required to understand the text.

    Args:
        prompt (str): The prompt given to the model.
        response (str, optional): The response generated by the model.
        threshold (float): The threshold for grade score (default is 5).

    Returns:
        dict: A dictionary containing the prompt, response, score containing the prompt grade score and
              response_grade_score, is_passed, and threshold.
    """
    prompt_grade_score = textstat.flesch_kincaid_grade(prompt)

    if response is not None:
        response_grade_score = textstat.flesch_kincaid_grade(response)
        is_passed = (
            True
            if prompt_grade_score < threshold and response_grade_score < threshold
            else False
        )
    else:
        response_grade_score = None
        is_passed = True if prompt_grade_score < threshold else False

    result = {
        "prompt": prompt,
        "response": response,
        "score": {
            "prompt_grade_score": prompt_grade_score,
            "response_grade_score": response_grade_score,
        },
        "is_passed": is_passed,
        "threshold": threshold,
    }
    return result