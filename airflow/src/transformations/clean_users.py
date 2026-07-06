def clean_user_data(df):
    """Example Pandas transformation helper for formatting data for OLAP analytics."""
    df['email'] = df['email'].str.strip().str.lower()
    df['username'] = df['username'].str.strip()
    return df
