CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    stars NUMERIC(10,2) DEFAULT 0,
    referrer BIGINT,
    refs INT DEFAULT 0
);

CREATE TABLE completed_tasks (
    user_id BIGINT,
    task_id TEXT,
    PRIMARY KEY (user_id, task_id)
);

CREATE TABLE withdrawals (
    id SERIAL PRIMARY KEY,
    user_id BIGINT,
    amount NUMERIC(10,2),
    status TEXT DEFAULT 'pending'
);
