# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*

- *Analyze costs, scalability, availability, and workflow*

  - Costs: App Service Plans are much cheaper as compared to Virtual Machines.
  - Scalabilty: App Services are auto-scalable.
  - Availablity: App Services provide high availablity.
  - Workflow: Easier to setup an app service (even with github actions workflow) than a virtual machine.
    
    
- *Choose the appropriate solution (VM or App Service) for deploying the app*

  - I will recommend App service for this kind of application deployment.
- *Justify your choice*

  - As the application isn't that complex and is written in Python which is a supported language for App Service Plans, I would like to use it for fast development.
  - The App service plans are cheaper with F1 being almost free.
  - We don't have to care about the underlying OS and its settings/configurations.
  - Allows Continous Deployment even using Github Actions Workflow.

### Assess app changes that would change your decision.

 - If the Application was any heavier which required high availability and scalability beyond the scopes of the largest App service, Maybe i would have opted for the Vitual Machine.
 - I would have been forced to choose virtual machines if the application was written in a language not supported by the App Service Plans or that language is not available or even for legacy application from on premise.
