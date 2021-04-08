# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*

- *Analyze costs, scalability, availability, and workflow*

  - Costs: App Service Plans are cheaper as compared to Virtual Machines.
  - Scalabilty: App Services are auto-scalable.
  - Availablity: App Services provide high availablity.
  - Workflow: Much easier to setup an app service (with github actions workflow) than a virtual machine.
    
    Note: Multiple VMs can be grouped together to provide better scalability and availability but that again, has an impact on economics of the app (costs).
    
- *Choose the appropriate solution (VM or App Service) for deploying the app*

  - I would choose an App service for a small application like this one.
- *Justify your choice*

  - As the application isn't that complex and is written in Python which is a supported language for App Service Plans, I would like to use it for fast development.
  - The App service plans are cheaper with F1 being almost free.
  - We don't have to care about the underlying OS and its settings/configurations.
  - Allows Continous Deployment using Github Actions Workflow.

### Assess app changes that would change your decision.

 - If the Application was any heavier which required high availability and scalability beyond the scopes of the largest App service, I would have opted for the Vitual Machine.
 - I would have been forced to choose virtual machines if the application was written in a language not supported by the App Service Plans.
