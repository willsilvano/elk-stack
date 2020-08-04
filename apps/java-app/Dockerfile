FROM maven:3.5.2-jdk-8-alpine AS MAVEN_BUILD
WORKDIR /build/
COPY pom.xml .
COPY src ./src
RUN mvn package

FROM openjdk:8-jdk-alpine
WORKDIR /app
COPY --from=MAVEN_BUILD /build/target/*.jar .
COPY elastic-apm-agent-1.18.0.RC1.jar .
RUN addgroup -g 1001 -S appuser \
    && adduser -u 1001 -S appuser -G appuser \
    && chown -R appuser:appuser /app
USER appuser
EXPOSE 8080
CMD java -javaagent:elastic-apm-agent-1.18.0.RC1.jar -Delastic.apm.service_name=JAVA_APP -Delastic.apm.application_packages=com.app -Delastic.apm.server_urls=http://apm-server:8200 -jar spring-boot-web.jar