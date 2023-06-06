CREATE TABLE IF NOT EXISTS tracking_best_model (
    experiment_id SERIAL PRIMARY KEY,
    experiment_datetime VARCHAR NOT NULL,
    cv_folds NUMERIC NOT NULL,
    batch_size NUMERIC NOT NULL,
    dropout FLOAT NOT NULL,
    epochs NUMERIC NOT NULL,
    learning_rate FLOAT NOT NULL,
    num_units NUMERIC NOT NULL,
    mean_test_score FLOAT NOT NULL,
    std_test_score FLOAT NOT NULL
);