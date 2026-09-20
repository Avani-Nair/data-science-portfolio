healthcare <- read.csv('healthcare_dataset.csv', header=T,na.strings=c(''))
View(healthcare)

data <- subset(healthcare, select = -c(1,3,4,6,7,8,11,13))

median.billing <- median(data$Billing.Amount)
cat('Median billing amount: $', round(median.billing, 2), '\n')

data$High.Cost <- ifelse(data$Billing.Amount > median.billing, 'Yes', 'No')
data$High.Cost <- as.factor(data$High.Cost)
data <- subset(data, select = -Billing.Amount)

data$Medical.Condition <- as.factor(data$Medical.Condition)
data$Insurance.Provider <- as.factor(data$Insurance.Provider)
data$Admission.Type <- as.factor(data$Admission.Type)
data$Medication <- as.factor(data$Medication)
data$Test.Results <- as.factor(data$Test.Results)

set.seed(456)

n = length(data$High.Cost)
nt = round(n*0.70)

index = sample(1:n, nt)

train = data[index, ]
test = data[-index, ]

install.packages('rpart')
install.packages('rpart.plot')

library('rpart')
library('rpart.plot')

mytree <- rpart(
  High.Cost ~ Age + Admission.Type + Medical.Condition + Medication + Test.Results + Insurance.Provider,
  data = train,
  method = "class")

rpart.plot(mytree, box.palette = "Blues")

pred <- predict(mytree, test, type = "class")

table(Predicted = pred, Actual = test$High.Cost)

pred <- predict(mytree, test, type = "class")

table(Predicted = pred, Actual = test$High.Cost)

conf <- table(Predicted = pred, Actual = test$High.Cost)

accuracy <- sum(diag(conf)) / sum(conf)

accuracy

precision <- diag(conf) / colSums(conf)

precision

recall <- diag(conf) / rowSums(conf)

recall
