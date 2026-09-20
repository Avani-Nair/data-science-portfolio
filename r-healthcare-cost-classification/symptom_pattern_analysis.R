install.packages('arules')
install.packages('arulesViz')

library('arules')
library('arulesViz')

data <- read.csv('symptoms_data_covid_like.csv')

head(data)

symptoms_data <- subset(data, select = -c(PatientID, cluster_label))

symptoms_data[] <- lapply(symptoms_data, function(x) x == 1)

trans_symptoms_data <- as(symptoms_data, 'transactions')

summary(trans_symptoms_data)

itemFrequencyPlot(trans_symptoms_data, topN = 12)

rules = apriori(
  trans_symptoms_data,
  parameter = list(support = 0.05, confidence = 0.60)
)

inspect(rules)

plot(rules, method = "scatterplot")
