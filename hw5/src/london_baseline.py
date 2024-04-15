# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
from tqdm import tqdm
import utils
import argparse

argp = argparse.ArgumentParser()
argp.add_argument("--corpus_path", default="birth_dev.tsv")
args = argp.parse_args()


def london_baseline(corpus_path):
    predictions = []
    for line in tqdm(open(corpus_path)):
            predictions.append("London")
    total, correct = utils.evaluate_places(corpus_path, predictions)
    
    return correct

print(london_baseline(args.corpus_path))
    
