package stepDefinitions;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class TransferFundsSteps {

    @Given("I am logged in to the testfire portal")
    public void i_am_logged_in_to_the_testfire_portal() {
        // Write code here that logs in to the testfire portal
    }

    @When("I click on the transfer funds link")
    public void i_click_on_the_transfer_funds_link() {
        // Write code here that clicks on the transfer funds link
    }

    @Then("I should be navigated to the transfer fund page")
    public void i_should_be_navigated_to_the_transfer_fund_page() {
        // Write code here that verifies if the user is on the transfer fund page
    }

    @Given("I am on the transfer fund page")
    public void i_am_on_the_transfer_fund_page() {
        // Write code here that verifies if the user is on the transfer fund page
    }

    @When("I select a different account in the \"From\" field")
    public void i_select_a_different_account_in_the_from_field() {
        // Write code here that selects a different account in the "From" field
    }

    @When("I select a different account in the \"To\" field")
    public void i_select_a_different_account_in_the_to_field() {
        // Write code here that selects a different account in the "To" field
    }

    @When("I enter the amount to transfer")
    public void i_enter_the_amount_to_transfer() {
        // Write code here that enters the amount to transfer
    }

    @When("I click on the transfer button")
    public void i_click_on_the_transfer_button() {
        // Write code here that clicks on the transfer button
    }

    @Then("the funds should be transferred successfully")
    public void the_funds_should_be_transferred_successfully() {
        // Write code here that verifies if the funds are transferred successfully
    }

    @When("I select the same account in the \"From\" and \"To\" fields")
    public void i_select_the_same_account_in_the_from_and_to_fields() {
        // Write code here that selects the same account in the "From" and "To" fields
    }

    @Then("the system should throw an error message")
    public void the_system_should_throw_an_error_message() {
        // Write code here that verifies if the system throws an error message
    }
}