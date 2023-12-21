```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class AddEmployeePage {
    private WebDriver driver;

    @FindBy(id = "firstName")
    private WebElement firstNameField;

    @FindBy(id = "lastName")
    private WebElement lastNameField;

    @FindBy(id = "employeeId")
    private WebElement employeeIdField;

    @FindBy(id = "btnSave")
    private WebElement saveButton;

    @FindBy(id = "success")
    private WebElement successMessage;

    public AddEmployeePage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public void enterFirstName(String firstName) {
        firstNameField.sendKeys(firstName);
    }

    public void enterLastName(String lastName) {
        lastNameField.sendKeys(lastName);
    }

    public void enterEmployeeId(String employeeId) {
        employeeIdField.sendKeys(employeeId);
    }

    public void clickSaveButton() {
        saveButton.click();
    }

    public String getSuccessMessage() {
        return successMessage.getText();
    }

    public void addEmployee(String firstName, String lastName, String employeeId) {
        enterFirstName(firstName);
        enterLastName(lastName);
        enterEmployeeId(employeeId);
        clickSaveButton();
    }
}
```