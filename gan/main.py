"""
To run Instructor
"""
import argparse
from instructor import Instructor

parser = argparse.ArgumentParser(description='')
parser.add_argument('-bert_model', type=str, default='', help='bert model string. used for training gan')
parser.add_argument('-data_in', type=str, default='', help='path to input data e.g. general_in* file')
parser.add_argument('-num_labels', type=int, default='',help='number of labels to classify')
parser.add_argument('-maxlen', type=int, default='',help='max sequence length')
parser.add_argument('-batch_size', type=int, default='',help='')
parser.add_argument('-lr', type=float, default='',help='learning rate (lr) for BertAdam')
parser.add_argument('-warmup', type=float, help='warmup value for BertAdam')
parser.add_argument('-epochs', type=int, help='number of iterations')
parser.add_argument('-model_out', type=str, default='', help='path to model dir')
parser.add_argument('-result_out', type=str, default='', help='path to result fi')
parser.add_argument('-loss_dir', type=str, default='', help='path to result loss dir')
parser.add_argument("-cuda", action="store_true", help="use gpu or not")

parser.add_argument("-test", action="store_true", help="valid/test if true")
parser.add_argument('-load_epoch', type=int, default=-1, help='0-indexed epoch of the model to load')
parser.add_argument('-seed', type=int, default=2809, help='random seeds')

args = parser.parse_args()
print(args)

instructor = Instructor(args)
if args.test:
    instructor.test()
else:
    instructor.train()