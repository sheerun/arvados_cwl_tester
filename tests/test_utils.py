from arvados_cwltest.helpers import *
from arvados_cwltest.arvados_connection import create_ouputs_dict, check_if_collection_output_not_empty, \
    basic_arvados_test


uuid = "arind-j7d0g-11cq990ue0u0cyg"

def test_load_file():
    assert type(load_file("./tests/cwl_workflows/test_single_step/test_single_step.cwl")) == list


def test_create_input_yml():
    create_input_yml(
        {
            "metaInfoFile": {
                "class": "File",
                "location": "keep:b05083d7db79c2e4e211dbef369e98a7+76/sampleList_E-MTAB-8208.txt",
            },
            "fastqCollection": {
                "class": "File",
                "location": "keep:00780063929dcd34186ae2394505202d+422439",
            }
        }
    )


def test_create_sinput_yml_empty():
    create_input_yml({})


# Example how to run this tests on some CommanLineTool
from datetime import datetime
def helper_single_step(input_name: str):
    run = basic_arvados_test(
        uuid,
        f'{input_name} {datetime.now():%Y-%m-%d %H:%M:%S%f%z} Monika',
        "./tests/cwl_workflows/test_single_step/test_single_step.cwl",
        {
            "name": input_name
            }
            )
    assert check_if_collection_output_not_empty(run)
    output_dict = create_ouputs_dict(run)
    assert input_name in output_dict
    assert output_dict[input_name]["size"] == 0
    assert output_dict[input_name]["basename"] == input_name

def test_step_single_step1():
    helper_single_step("example1.txt")

def test_step_single_step2():
    helper_single_step("example2.txt")

def test_step_single_step3():
    helper_single_step("example3.txt")

def test_step_single_step4():
    helper_single_step("example4.txt")

def test_step_single_step5():
    helper_single_step("example5.txt")

def test_step_single_step6():
    helper_single_step("example6.txt")

def test_step_single_step7():
    helper_single_step("example7.txt")

def test_step_single_step8():
    helper_single_step("example8.txt")

def test_step_single_step9():
    helper_single_step("example9.txt")

def test_step_single_step10():
    helper_single_step("example10.txt")

def test_step_single_step10():
    helper_single_step("example11.txt")