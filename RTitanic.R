setwd('~/titanic')

library(dplyr)
library(ggplot2)

test <- read.csv('test.csv', encoding = "UTF-8")
train <- read.csv('train.csv', encoding = "UTF-8")
gender_submission <- read.csv('gender_submission.csv', encoding = "UTF-8")

testGS <- test
testGS$Survived <- gender_submission$Survived
t_columns <- colnames(train)
testGS <- testGS[, t_columns]

titanic_passengers <- union(train,testGS)

dim(titanic_passengers)
names(titanic_passengers)
str(titanic_passengers)
n_t = nrow(titanic_passengers)

library(funModeling)
df_status(titanic_passengers)


#on recherche les valeurs manquantes

sapply(titanic_passengers,function(x) sum(x == "" | is.na(x)))
sapply(titanic_passengers,function(x) sum(x == "" | is.na(x))/nrow(titanic_passengers)*100)

#on supprime la colonne 'Cabin'
titanic_pas <- select(titanic_passengers,-Cabin)
titanic_pas$Age[is.na(titanic_pas$Age)] <- median(titanic_pas$Age,na.rm=TRUE)
sapply(titanic_pas,function(x) sum(x == "" | is.na(x)))

#on supprimes les lignes ayant des valeurs manquantes 'NA'
titanic_pas <- na.omit(titanic_pas)
n1 <- nrow(titanic_pas)
n_t - n1 
sapply(titanic_pas,function(x) sum(x == "" | is.na(x)))

#on supprime les dernières lignes ayant des valeurs manquantes
unique(titanic_pas$Embarked)
values_embarked <- c(unique(titanic_pas$Embarked))
values_embarked
titanic_pas <- titanic_pas[(titanic_pas$Embarked == 'S' | titanic_pas$Embarked == 'C' | titanic_pas$Embarked == 'Q'),]
sapply(titanic_pas,function(x) sum(x == "" | is.na(x)))
titanic_pas <- na.omit(titanic_pas)




#on crée d'emblee un autre dataframe avec les valeurs manquantes
# de l'age remplacees par la moyenne
titanic_pas_mean <- select(titanic_passengers,-Cabin)
titanic_pas_mean$Age[is.na(titanic_pas_mean$Age)] <- mean(titanic_pas_mean$Age,na.rm=TRUE)
sapply(titanic_pas_mean,function(x) sum(x == "" | is.na(x)))
titanic_pas_mean <- titanic_pas_mean[(titanic_pas_mean$Embarked == 'S' | titanic_pas_mean$Embarked == 'C' | titanic_pas_mean$Embarked == 'Q'),]
sapply(titanic_pas_mean,function(x) sum(x == "" | is.na(x)))
titanic_pas_mean <- na.omit(titanic_pas_mean)


#-----------------------------------------------

write.csv(x = titanic_pas, file = "~/titanic/titanic_passengers_median.csv")
write.csv(x = titanic_pas_mean, file = "~/titanic/titanic_passengers_mean.csv")


#-----------------------------------------------

#histogramme survie fonction de l' age
histo_age <- ggplot(titanic_pas, aes(x=Age, fill=Sex, color=Sex)) + 
  geom_histogram(fill='white', alpha=0.5, position="dodge") +
  theme(legend.position="top")
histo_age


histo_survie <- ggplot(titanic_pas, aes(x=Survived, fill=Sex, color=Sex)) + 
  geom_histogram(fill='white', alpha=0.5, position="dodge") +
  scale_color_manual(values=c("#999999", "#E69F00", "#56B4E9"))+
  scale_fill_manual(values=c("#999999", "#E69F00", "#56B4E9"))
  #theme(legend.position="top")
histo_survie
 










#-----------------------------------------------

#Test hypothese traitement enfants
nombre_enfants <- titanic_pas %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age < 18) %>%
  count()
nb_enfants <- 154

nombre_enfants18 <- nombre_enfants %>%
  filter(nombre_enfants$Age == 17.00)
dim(nombre_enfants18)

nombre_enfants2 <- titanic_pas %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age < 17)
dim(nombre_enfants2)

nombre_enfants_survivants <- titanic_pas %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age < 18) %>%
  group_by(Survived)%>%
  count()

nombres_deces <- titanic_pas %>%
  select(PassengerId, Survived) %>%
  group_by(Survived)%>%
  count()

nombre_adultes_survivants <- titanic_pas %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age >= 18) %>%
  group_by(Survived)%>%
  count()


matrice_enfants= matrix(c(78,76, 414, 738), 2, 2, byrow=TRUE)
rownames(matrice_enfants) = c("Enfants", "Adultes")
colnames(matrice_enfants) = c("Survivants", "Decedes")
tab_enfants = as.table(matrice_enfants)
tab_enfants
(enfants_chisq = chisq.test(tab_enfants, simulate.p.value = TRUE))


#Test hypothese traitement femmes
nombre_genre <- titanic_pas %>%
  select(PassengerId, Survived, Sex) %>%
  group_by(Sex, Survived)%>%
  count()

matrice_femmes= matrix(c(383,81, 109, 733), 2, 2, byrow=TRUE)
rownames(matrice_femmes) = c("Femmes", "Hommes")
colnames(matrice_femmes) = c("Survivant.e.s", "Decede.e.s")
tab_genre = as.table(matrice_femmes)
tab_genre

(femmes_chisq = chisq.test(tab_genre, simulate.p.value = TRUE))


#-----------------------------------------------

#test T de Student pour prix des billets
#on cree deux vecteurs avec les valeurs des billets 
# pour les passagers survivants et disparus respectivement
fare_survived <- titanic_pas %>%
  select(Survived, Fare) %>%
  filter(Survived == 1) %>%
  select(Fare)

fare_dead <- titanic_pas %>%
  select(Survived, Fare) %>%
  filter(Survived == 0) %>%
  select(Fare)

var(fare_survived)
var(fare_dead)

ks.test(fare_survived, "pnorm")

fare_survived2 <- sapply(fare_survived,function(x) as.numeric(x))
fare_dead2 <- sapply(fare_dead,function(x) as.numeric(x))

shapiro.test(fare_survived2)
#la p-value est tres basse
#on ne peut que rejeter l'hypothèse de la normalité

histo_fare_survived <- ggplot(fare_survived, aes(x=Fare)) + 
  geom_histogram() +
  theme(legend.position="top")
histo_fare_survived

histo_fare_dead <- ggplot(fare_dead, aes(x=Fare)) + 
  geom_histogram() +
  theme(legend.position="top")
histo_fare_dead






#Tests avec dataset train---------------------------

#Test hypothese traitement enfants
nombre_enfants_train <- train %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age < 18) %>%
  count()
nb_enfants_train <- 113

#nombre_enfants18 <- nombre_enfants %>%
  filter(nombre_enfants$Age == 17.00)
dim(nombre_enfants18)

#nombre_enfants2 <- titanic_pas %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age < 17)
dim(nombre_enfants2)

nombre_enfants_survivants_train <- train %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age < 18) %>%
  group_by(Survived)%>%
  count()

nombres_deces_train <- train %>%
  select(PassengerId, Survived) %>%
  group_by(Survived)%>%
  count()

nombre_adultes_survivants_train <- train %>%
  select(PassengerId, Survived, Age) %>%
  filter(Age >= 18) %>%
  group_by(Survived)%>%
  count()


matrice_enfants_train= matrix(c(61, 52, 229, 372), 2, 2, byrow=TRUE)
rownames(matrice_enfants_train) = c("Enfants", "Adultes")
colnames(matrice_enfants_train) = c("Survivants", "Decedes")
tab_enfants_train = as.table(matrice_enfants_train)
tab_enfants_train
(enfants_train_chisq = chisq.test(tab_enfants_train, simulate.p.value = TRUE))


#Test hypothese traitement femmes
nombre_genre_train <- train %>%
  select(PassengerId, Survived, Sex) %>%
  group_by(Sex, Survived)%>%
  count()

matrice_femmes_train= matrix(c(233, 81, 109, 468), 2, 2, byrow=TRUE)
rownames(matrice_femmes_train) = c("Femmes", "Hommes")
colnames(matrice_femmes_train) = c("Survivant.e.s", "Decede.e.s")
tab_genre_train = as.table(matrice_femmes_train)
tab_genre_train

(femmes_train_chisq = chisq.test(tab_genre_train, simulate.p.value = TRUE))


#-----------------------------------------------

#test avec train dataset
#test T de Student pour prix des billets
#on cree deux vecteurs avec les valeurs des billets 
# pour les passagers survivants et disparus respectivement
fare_survived_train <- train %>%
  select(Survived, Fare) %>%
  filter(Survived == 1) %>%
  select(Fare)

fare_dead_train <- train %>%
  select(Survived, Fare) %>%
  filter(Survived == 0) %>%
  select(Fare)

var(fare_survived_train)
var(fare_dead_train)

ks.test(fare_survived_train, "pnorm")
#'aucun ex-aequo ne devrait être présent pour le test de Kolmogorov-Smirnov'

fare_survived_train2 <- sapply(fare_survived,function(x) as.numeric(x))
fare_dead_train2 <- sapply(fare_dead,function(x) as.numeric(x))

shapiro.test(fare_survived_train2)
#la p-value est tres basse
#on ne peut que rejeter l'hypothèse de la normalité

histo_fare_survived_train <- ggplot(fare_survived_train, aes(x=Fare)) + 
  geom_histogram() +
  theme(legend.position="top")
histo_fare_survived_train

histo_fare_dead_train <- ggplot(fare_dead_train, aes(x=Fare)) + 
  geom_histogram() +
  theme(legend.position="top")
histo_fare_dead_train


#test de Wilcoxon
wilcox.test(fare_survived_train2, fare_dead_train2)








