import quanchecker

test_cases = [
    {
        'checking_method': quanchecker.response_contain_check,
        'url': "http://localhost:(port)/item/item 1",
        'header': {},
        'method': 'GET',
        'body': "",
        'expected': "item 1",
    },
    {
        'checking_method': quanchecker.response_contain_check_inverse,
        'url': "http://localhost:(port)/item/{{ 7 * 7}}",
        'header': {},
        'method': 'GET',
        'body': "",
        'expected': "49",
    },
    {
        'checking_method': quanchecker.response_contain_check,
        'url': "http://localhost:(port)/item/{{ 7 * 7}}",
        'header': {},
        'method': 'GET',
        'body': "",
        'expected': "7",
    },
    {
        'checking_method': quanchecker.response_contain_check_inverse,
        'url': "http://localhost:(port)/item/{{ 121 * 39}}",
        'header': {},
        'method': 'GET',
        'body': "",
        'expected': "19",
    },
    {
        'checking_method': quanchecker.response_contain_check_inverse,
        'url': "http://localhost:(port)/item/{{ config.items() }}",
        'header': {},
        'method': 'GET',
        'body': "",
        'expected': "SECRET_KEY",
    },
]

quanchecker.run_tests_dev(test_cases)