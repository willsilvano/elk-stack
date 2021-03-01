FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create index
# CMD ["elastalert-create-index"]

# Test rule
# CMD ["elastalert-test-rule", "rules/uptime.yaml"]

# Run 
CMD ["elastalert", "--verbose"]