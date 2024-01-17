import cucumber.api.java.en.Given;
import cucumber.api.java.en.When;
import cucumber.api.java.en.Then;

public class TransferFundsSteps {

    @Given("I am logged in to the testfire portal")
    public void i_am_logged_in_to_the_testfire_portal() {
        // implementation goes here
    }

    @When("I click on the \"Transfer Funds\" link")
    public void i_click_on_the_transfer_funds_link() {
        // implementation goes here
    }

    @Then("I should be navigated to the transfer funds page")
    public void i_should_be_navigated_to_the_transfer_funds_page() {
        // implementation goes here
    }

    @Given("I am on the transfer funds page")
    public void i_am_on_the_transfer_funds_page() {
        // implementation goes here
    }

    @When("I select \"(.*)\" in the \"From\" field")
    public void i_select_from_account_in_the_from_field(String fromAccount) {
        // implementation goes here
    }

    @When("I select \"(.*)\" in the \"To\" field")
    public void i_select_to_account_in_the_to_field(String toAccount) {
        // implementation goes here
    }

    @When("I enter \"(.*)\" in the \"Amount\" field")
    public void i_enter_amount_in_the_amount_field(String amount) {
        // implementation goes here
    }

    @When("I click on the \"Transfer\" button")
    public void i_click_on_the_transfer_button() {
        // implementation goes here
    }

    @Then("I should see a success message")
    public void i_should_see_a_success_message() {
        // implementation goes here
    }

    @When("I select the same account \"(.*)\" in the \"From\" and \"To\" fields")
    public void i_select_the_same_account_in_the_from_and_to_fields(String account) {
        // implementation goes here
    }

    @Then("I should see an error message")
    public void i_should_see_an_error_message() {
        // implementation goes here
    }
}