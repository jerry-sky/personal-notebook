---
lang: 'en-GB'
title: 'Cloud'
author: 'Jerry Sky'
---

- [AWS](#aws)
    - [Compute](#compute)
    - [Storage](#storage)
    - [Databases](#databases)
    - [Migration](#migration)
    - [Networking & Content Delivery](#networking--content-delivery)
    - [Developer Tools](#developer-tools)
    - [Management Tools](#management-tools)
    - [Analytics](#analytics)
    - [Security, Identity, and Compliance](#security-identity-and-compliance)
    - [Application Services](#application-services)
    - [Mobile Services](#mobile-services)
    - [Business Productivity](#business-productivity)
    - [Artificial Intelligence](#artificial-intelligence)
    - [Customer Engagement](#customer-engagement)
    - [Game Development](#game-development)
    - [Internet of Things](#internet-of-things)

---

## AWS

_List of web services offered by Amazon._

[Original article](https://medium.com/@kunalyadav/what-is-aws-and-what-can-you-do-with-it-395b585b03c)

### Compute
1. EC2 (Elastic Compute Cloud) — These are just the virtual machines in the cloud on which you have the OS level control. You can run whatever you want in them.
2. LightSail — If you don’t have any prior experience with AWS this is for you. It automatically deploys and manages compute, storage and networking capabilities required to run your applications.
3. ECS (Elastic Container Service) — It is a highly scalable container service to allows you to run Docker containers in the cloud.
4. EKS (Elastic Container Service for Kubernetes) — Allows you to use Kubernetes on AWS without installing and managing your own Kubernetes control plane. It is a relatively new service.
5. Lambda — AWS’s serverless technology that allows you to run functions in the cloud. It’s a huge cost saver as you pay only when your functions execute.
6. Batch — It enables you to easily and efficiently run batch computing workloads of any scale on AWS using Amazon EC2 and EC2 spot fleet.
7. Elastic Beanstalk — Allows automated deployment and provisioning of resources like a highly scalable production website.

### Storage
1. S3 (Simple Storage Service) — Storage service of AWS in which we can store objects like files, folders, images, documents, songs, etc. It cannot be used to install software, games or Operating System.
2. EFS (Elastic File System) — Provides file storage for use with your EC2 instances. It uses NFSv4 protocol and can beused concurrently by thousands of instances.
3. Glacier — It is an extremely low-cost archival service to store files for a long time like a few years or even decades.
4. Storage Gateway — It is a virtual machine that you install on your on-premise servers. Your on-premise data can be backed up to AWS providing more durability.

### Databases
1. RDS (Relational Database Service) — Allows you to run relational databases like MySQL, MariaDB, PostgreSQL, Oracle or SQL Server. These databases are fully managed by AWS like installing antivirus and patches.
2. DynamoDB — It is a highly scalable, high-performance NoSQL database. It provides single-digit millisecond latency at any scale.
3. Elasticache — It is a way of caching data inside the cloud. It can be used to take load off of your database by caching most frequent queries.
4. Neptune — It has been launched recently. It is a fast, reliable and scalable graph database service.
5. RedShift — It is AWS’s data warehousing solution that can be used to run complex OLAP queries.

### Migration
1. DMS (Database Migration Service) — It can be used to migrate on-site databases to AWS. It also allows you to migrate from one type of database to another. Eg -from Oracle to MySQL.
2. SMS (Server Migration Service) — It allows you to migrate on-site servers to AWS easily and quickly.
3. Snowball — It is a briefcase sized appliance that can be used to send terabytes of data inside and outside of AWS.

### Networking & Content Delivery
1. VPC (Virtual Private Cloud) — It is simply a data center in the cloud in which you deploy all your resources. It allows you to better isolate your resources and secure them.
2. CloudFront -It is AWS’s Content Delivery Network (CDN) that consists of Edge locations that cache resources.
3. Route53 — It is AWS’s highly available DNS (Domain Name System) service. You can register domain names through it.
4. Direct Connect — Using it you can connect your data center to an Availability zone using a high speed dedicated line.
5. API Gateway — Allows you to create, store and manage APIs at scale.

### Developer Tools
1. CodeStar — It is a cloud-based service for creating, managing, and working with software development projects on AWS. You can quickly develop, build, and deploy applications on AWS with an AWS CodeStar project.
2. CodeCommit — It is AWS’s version control service that allows you to store your code and other assets privately in the cloud.
3. CodeBuild — It automates the process of building (compiling) your code.
4. CodeDeploy — It is a way of deploying your code in EC2 instances automatically.
5. CodePipeline — Allows you to keep track of different steps in your deployment like building, testing, authentication, and deployment on development and production environments.
6. Cloud9 —It is an IDE (Integrated Development Environment) for writing, running, and debugging code in the cloud.
7. X-Ray — It makes it easy for developers to analyze the behavior of their distributed applications by providing request tracing, exception collection, and profiling capabilities.

### Management Tools
1. CloudWatch — It can be used to monitor AWS environments like CPU utilization of EC2 and RDS instances and trigger alarms based on different metrics.
2. CloudFormation — It is a way of turning infrastructure into the cloud. You can use templates to provision a whole production environment in minutes.
3. CloudTrail — A way of auditing AWS resources. It logs all changes and API calls made to AWS.
4. OpsWorks — It helps in automating Chef deployments on AWS.
5. Config — It monitors your environment and notifies you when you break certain configurations.
6. Service Catalog — For larger enterprises, helps to authorize which services will be used and which won’t be.
7. Trusted Advisor — Gives you recommendations on how to do cost optimizations, and secure your environment.
8. AWS Auto Scaling — Allows you to automatically scale your resources up and down based on CloudWatch metrics.
9. Systems Manager — Allows you to group your resources, so you can quickly gain insights, identify issues and act on them.
10. Managed Services—It provides ongoing management of your AWS infrastructure so you can focus on your applications.

### Analytics
1. Athena — Allows you to run SQL queries on your S3 bucket to find files.
2. EMR (Elastic Map Reduce) — It is used for big data processing like Hadoop, Apache Spark, and Splunk, etc.
3. CloudSearch — It can be used to create a fully managed search engine for your website.
4. ElasticSearch — It is similar to CloudSearch but gives you more features like application monitoring.
5. Kinesis — A way of streaming and analyzing real-time data at massive scale. It can store TBs of data per hour.
6. Data Pipeline — Allows you to move data from one place to another. Eg: from S3 to DynamoDB or vice versa.
7. QuickSight —A business analytics tool that allows you to create visualizations in a rich dashboard for data in AWS. Eg: for S3, DynamoDB, etc.
8. Glue — It is a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores.

### Security, Identity, and Compliance
1. IAM (Identity and Access Management) — Allows you to manage users, assign policies, create groups to manage multiple users.
2. Inspector — It is an agent that you install on our virtual machines, which then reports any security vulnerabilities.
3. Certificate Manager — It gives free SSL certificates for your domains that are managed by Route53.
4. Directory Service — A way of using your company’s account to log in to AWS.
5. WAF (Web Application Firewall) — Gives you application-level protection and blocks SQL injection and cross-site scripting attacks.
6. CloudHSM — It helps you meet corporate, contractual, and regulatory compliance requirements for data security by using dedicated Hardware Security Module (HSM) appliances within the AWS Cloud.
7. Cloud Directory — It enables you to build flexible, cloud-native directories for organizing hierarchies of data along multiple dimensions.
8. KMS (Key Management Service) — It is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
9. Organizations — It allows you to create groups of AWS accounts that you can use to more easily manage security and automation settings.
10. Shield — A managed DDoS (Distributed Denial of Service) protection service that safeguards web applications running on AWS.
11. Artifact — It is the place where you can get all your compliance certifications.
12. Macie — A data visibility security service that helps classify and protect your sensitive and business-critical content.
13. GuardDuty —Provides intelligent threat detection to protect your AWS accounts and workloads

### Application Services
1. Step Functions — A way of visualizing what’s going inside your application and what different microservices it is using.
2. SWF (Simple Workflow Service) — A way of coordinating both automated tasks and human-led tasks.
3. SNS (Simple Notification Service) — Can be used to send you notifications in the form of email and SMS regarding your AWS services. It is a push-based service.
4. SQS (Simple Queue Service) — The first service offered by AWS. It can be used to decouple your applications. It is a pull-based service.
5. Elastic Transcoder — Changes a video’s format and resolution to support different devices like tablets, smartphones, and laptops of different resolutions.

### Mobile Services
1. Mobile Hub — Allows you to add, configure and design features for mobile apps. It is a console for mobile app development.
2. Cognito — Allows your users to signup using social identity providers.
3. Device Farm — Enables you to improve quality of apps by quickly testing on hundreds of mobile devices.
4. AWS AppSync —It is an enterprise level, fully managed GraphQL service with real-time data synchronization and offline programming features.
5. Mobile Analytics — Allows to simply and cost effectively analyze mobile data.

### Business Productivity
1. Alexa for Business — It lets you empower your organization with voice, using Alexa. Allows you to build custom voice skills for your organization.
2. Chime — Can be used for online meeting and video conferencing.
3. WorkDocs — Helps to store documents in the cloud
4. WorkMail — Allows you to send and receive business emails.
5. Desktop & App Streaming
6. WorkSpaces — It is a VDI (Virtual Desktop Infrastructure). Allows you to use remote desktops in the cloud
7. AppStream 2.0 — A way of streaming desktop applications to your users in the web browser. Eg: Using MS Word in Google Chrome.

### Artificial Intelligence
1. Lex — Allows you to quickly build chatbots.
2. Polly — AWS’s text-to-speech service. You can create audio versions of your notes using it.
3. Machine learning — You just have to give your dataset and target variable and AWS will take care of training your model.
4. Rekognition — AWS’s face recognition service. Allows you to recognize faces and object in images and videos.
5. SageMaker — Helps you to build, train and deploy machine learning models at any scale.
6. Comprehend — It is a Natural Language Processing (NLP) service that uses machine learning to find insights and relationships in text. It can be used for sentiment analysis.
7. Transcribe — It is the opposite of Polly. It is AWS’s speech-to-text service that provides that provides high-quality and affordable transcriptions.
8. Translate — It is like Google Translate and allows you to translate text in one language to another.
9. AR & VR (Augmented Reality & Virtual Reality)
10. Sumerian — It is a set of tools for creating high-quality virtual reality (VR) experiences on the web. You can quickly create interactive 3D scenes and publish it as a website for users to access.

### Customer Engagement
1. Amazon Connect — Allows you to create a customer care center in the cloud.
2. Pinpoint — It is like Google analytics for mobile applications. It helps you to understand users and engage with them.
3. SES (Simple Email Service) — Allows you to send bulk emails to your customers at an extremely low price.

### Game Development
1. GameLift — It is a service managed by AWS that can used to host dedicated game servers. It seamlessly scales without taking your game offline.

### Internet of Things
1. IoT Core— It is a managed cloud platform that lets connected devices — cars, light bulbs, sensor grids, and more — easily and securely interact with cloud applications and other devices.
2. IoT Device Management — Allows you to manage your IoT devices at any scale.
3. IoT Analytics — Can be used to perform analysis on data collected by your IoT devices.
4. Greengrass — Lets your IoT devices to process the locally generated data while advantage of AWS services.
5. Amazon FreeRTOS — It is a real-time operating system for microcontrollers that makes it easy to securely connect IoT devices locally or to the cloud.
