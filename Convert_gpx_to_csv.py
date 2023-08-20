from gpx_converter import Converter
import os
import argparse


def convert_gpx_to_csv(gpx_file, csv_file):
    """
    This function convert the gpx data to a csv file.

    Arguments:
    gpx_file: file with gpx data.

    Return:
    pass_result: a bool data that indicate if the converssion was succesfull
    position_data_csv: csv file with data about latitude, longitude and attitude
    """

    pass_result = Converter(input_file=gpx_file).gpx_to_csv(output_file=csv_file)

    return pass_result


def get_comline_parser():
    parser = argparse.ArgumentParser(description="Search files")
    parser.add_argument(
        "--path", type=str, default=".", help="Path where found the files"
    )

    return parser


if __name__ == "__main__":
    args = get_comline_parser().parse_args()

    for file_ in os.listdir(args.path):
        name, extension = os.path.splitext(file_)

        if extension in [".gpx"]:
            gpx_file = name + extension
            csv_file = name + ".csv"
            print("I found the file {}".format(gpx_file))

            pass_result = convert_gpx_to_csv(gpx_file, csv_file)
            if pass_result:
                print("file {} converted to .csv".format(gpx_file))
