
# Basics
R        | pandas
-------- | --------
dim(df)  | df.shape
head(df) | df.head()
summary(df)                      | df.describe()
filter(df, col1 == 1, col2 == 1) | df.query('col1 == 1 & col2 == 1')
df[df$col1 == 1 & df$col2 == 1, ]| df[(df.col1 == 1) & (df.col2 == 1)]
subset(df, col1 <= col2)         | df.loc[df.col1 <= df.col2]
select(df, col1, col3)           | df[['col1', 'col3']]
select(df, col1:col3)            | df.loc[:, 'col1':'col3']
distinct(select(df, col1, col2)) | df[['col1', 'col2']].drop_duplicates()
sample_n(df, 10)                 | df.sample(n=10)
sample_frac(df, 0.2)             | df.sample(frac=0.2)
arrange(df, col1, col2)          | df.sort_values(['col1','col2'])
arrange(df, desc(col1))          | df.sort_values('col1', ascending = False)
mutate(df, col4 = col1 - col2)   | df.assign(col4 = df.col1 - df.col2)
gdf <- group_by(df, col1)        | df.group_by('col1')
summarise(gdf, avg=mean(col1, na.rm=True)) |df.group_by('col1').agg({'col1': 'mean'})
summarise(gdf, total=sum(col1))            |df.group_by('col1').sum()
with(df, a+b)                    | df.eval('a+b') or df.a + df.b
melt(df, id = c('first', 'last'))| pd.melt(df, id_vars = ['first','last']

# Data Reshaping
## Pivot 
```
df.pivot(index='date', columns='person_id', values='sale_amount')
pivoted = df.pivot('date', 'person_id')
pivoted['sale_amount']
pivoted['sale_count']
```
If values argument is omitted, then we get a result dataframe grouped by index and columns for each of the rest variables.

## Stack and Unstack
When the dataframe is multi-indexed.
```
stacked = df.stack() # pivot a level of column labels into a level of index
stacked.unstack(0)   # pivot the 0 level index into column labels

df.stack(levels=['year','month']) 
stacked.unstack('month')
```

## Melt
Wide formats to long formats.
df.melt(id_vars = ['first', 'last'], var_name='quantity', value_name='values')

## Pivot tables
pivot() provides general pivoting, pivot_table() provides pivoting with aggregation of numeric data.
```
df.pivot_table(index='date', columns='person_id', values='sale_amount', aggfunc='sum')
df1.pivot_table(index=['a','b'], columns='c', values=['d','e'], margins=True, aggfunc='sum')
```
index specifies row labels, columns specifies column labels, 
values specifies variables we're applying the aggregation function to group by row and column labels. 
margins=True give column totals and row totals for each group.\

