FROM maven:3.5.2-jdk-8-alpine AS MAVEN_BUILD
WORKDIR /build/
COPY pom.xml .
COPY src ./src
RUN mvn package

FROM openjdk:8-jdk-alpine
WORKDIR /app
COPY --from=MAVEN_BUILD /build/target/*.jar .
RUN addgroup -g 1001 -S appuser \
    && adduser -u 1001 -S appuser -G appuser \
    && chown -R appuser:appuser /app
USER appuser
EXPOSE 8080
ENTRYPOINT ["java","-jar","spring-boot-web.jar"]