from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn.model_selection import train_test_split


def eval_metrics(actual, pred):
    precision = precision_score(actual, pred, average='weighted')
    recall = recall_score(actual, pred, average='weighted')
    accuracy = accuracy_score(actual, pred)
    f1 = f1_score(actual, pred, average='weighted')
    return {
        'precision': precision,
        'recall': recall,
        'accuracy': accuracy,
        'f1': f1
    }


def data_split(X, y):
    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3,
                                                        stratify=y, random_state=40, shuffle=True)
    return train_x, test_x, train_y, test_y

