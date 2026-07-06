def daily_signup_counts(df):
    """Aggregates signs ups by date for reporting."""
    return df.groupby('created_at').size().reset_index(name='signup_count')
