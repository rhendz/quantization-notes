# setup.py
import os


def create_directories():
    data_dir = "data"
    output_dir = "output"
    results_dir = os.path.join(output_dir, "results")

    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)


def main():
    create_directories()


if __name__ == "__main__":
    main()
