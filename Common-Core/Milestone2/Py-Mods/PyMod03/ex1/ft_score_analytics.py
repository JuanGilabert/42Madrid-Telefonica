import sys


def ft_is_valid_score(argv_score: str) -> bool:
    try:
        int(argv_score)
    except Exception:
        print(f"Invalid parameter: '{argv_score}'")
        return False
    return True


def ft_process_scores() -> list[int]:
    sys_argv_len: int = len(sys.argv)
    if sys_argv_len < 2:
        return []
    index: int = 0
    invalid_scores_count: int = 0
    scores_list_len: int = sys_argv_len - 1
    scores_list: list[int] = [0] * scores_list_len
    for argument in sys.argv[1:]:
        if ft_is_valid_score(argument):
            scores_list[index] = int(argument)
            index += 1
        else:
            invalid_scores_count += 1
    if not index:
        return []
    return scores_list[:scores_list_len - invalid_scores_count]


def ft_show_processed_scores(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {(sum(scores) / len(scores)):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    print()


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    processed_scores: list[int] = ft_process_scores()
    if not processed_scores:
        usage_msg = "python3 ft_score_analytics.py <score1> <score2>"
        return print(f"No scores provided. Usage: {usage_msg} ...")
    ft_show_processed_scores(processed_scores)


if __name__ == "__main__":
    try:
        ft_score_analytics()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
