import sys
import pandas as pd
import numpy as np

from sklearn.preprocessing import Binarizer, MaxAbsScaler, MinMaxScaler
from sklearn.preprocessing import Normalizer, PolynomialFeatures, RobustScaler, StandardScaler
from sklearn.decomposition import FastICA, PCA
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.cluster import FeatureAgglomeration
from sklearn.feature_selection import SelectFwe, SelectPercentile, VarianceThreshold
from sklearn.feature_selection import SelectFromModel, RFE
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.naive_bayes import GaussianNB
from evaluate_model import evaluate_model

dataset = sys.argv[1]
num_param_combinations = int(sys.argv[2])
random_seed = int(sys.argv[3])
preprocessor_num = int(sys.argv[4])

np.random.seed(random_seed)

preprocessor_list = [Binarizer, MaxAbsScaler, MinMaxScaler, Normalizer,
                     PolynomialFeatures, RobustScaler, StandardScaler,
                     FastICA, PCA, RBFSampler, Nystroem, FeatureAgglomeration,
                     SelectFwe, SelectPercentile, VarianceThreshold,
                     SelectFromModel, RFE]

chosen_preprocessor = preprocessor_list[preprocessor_num]

pipeline_components = [chosen_preprocessor, GaussianNB]
pipeline_parameters = {}
pipeline_parameters[GaussianNB] = [{}]

if chosen_preprocessor is SelectFromModel:
    pipeline_parameters[SelectFromModel] = [{'estimator': ExtraTreesClassifier(n_estimators=100, random_state=324089)}]
elif chosen_preprocessor is RFE:
    pipeline_parameters[RFE] = [{'estimator': ExtraTreesClassifier(n_estimators=100, random_state=324089)}]

evaluate_model(dataset, pipeline_components, pipeline_parameters)
