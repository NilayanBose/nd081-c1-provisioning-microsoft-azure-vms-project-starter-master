# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*

- *Analyze costs, scalability, availability, and workflow*

  - Costs: App Service Plans are much cheaper as compared to Virtual Machines.
  - Scalabilty: App Services are auto-scalable. When you are using App Service, you can scale your apps by scaling the App Service plan they run on. When multiple apps are run in the same App Service plan, each scaled-out instance runs all the apps in the plan. In This way, an App Service plan can be scaled to 10 instances.
  - Availablity: App Services provide high availablity with of 99.5% SLA uptime, apps can be hosted anywhere manually or automatically on Microsoft’s global datacenter infrastructure.
  - Workflow: Easier to setup an app service (even with github actions workflow) than a virtual machine also provides didifferent tools integration like Visual Studio.
    
    
- *Choose the appropriate solution (VM or App Service) for deploying the app*

  - I will recommend App service for this kind of application deployment even app service provides 99.5% uptime with versetile framework support and highly secure web app development.
- *Justify your choice*

  - As the application isn't that complex and is written in Python which is a supported language for App Service Plans, I would like to use it for fast development.
  - The App service plans are cheaper with F1 being almost free.
  - We don't have to care about the underlying OS and its settings/configurations.
  - Allows Continous Deployment even using Github Actions Workflow.

### Assess app changes that would change your decision.

 - If the Application was any heavier which required high availability and scalability beyond the scopes of the largest App service, Maybe i would have opted for the Vitual Machine.
 - I would have been forced to choose virtual machines if the application was written in a language not supported by the App Service Plans or that language is not available or even for legacy application from on premise.
