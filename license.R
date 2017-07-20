install.packages('RMySQL')

library(RMySQL)
conn = dbConnect(MySQL(),user = "root",password = "",dbname = "registry")
count <- fetch(res = dbSendQuery(conn, "select sum(count) from license where count > 50 group by tags"))
dbClearResult(dbListResults(conn)[[1]])
license <- fetch(res = dbSendQuery(conn, "select tags from license where count > 50 group by tags"))
dbClearResult(dbListResults(conn)[[1]])
# pie(as.vector(as.matrix(count)), labels = as.vector(as.matrix(license)))

count <- as.vector(as.matrix(count))
license <- as.vector(as.matrix(license))

piepercent <- round(100 * count / sum(count), 1)

piepercent <- paste(piepercent, "%", sep = "")

pie(count,labels = piepercent, main = "Most Popular Licenses", col = terrain.colors(length(count)))

legend("topright", license, cex = 0.8, fill = terrain.colors(length(count)))


dbClearResult(dbListResults(conn)[[1]])
