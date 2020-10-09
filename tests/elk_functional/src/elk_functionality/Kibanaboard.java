package elk_functionality;
import java.sql.Driver;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.Test;

import elk_functional_utilities.*;

public class Kibanaboard extends DriverUtil {

	
	
	WebDriver driver = getdriver();
	WebDriverWait wait=new WebDriverWait(driver, 100);
	@Test
	public void filemetricbeat() {
		try {
		driver.get(Kibana.Url);
		driver.manage().window().maximize();
		
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"kibana-body\"]/div/header/div/div[1]/div[1]/button"))).click();
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Dashboard"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"kibana-body\"]/div/header/div/div[1]/div[1]/button"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Discover"))).click();
		
		//Explore Filebeat
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"discover-sidebar\"]/div/discover-sidebar/section/div[1]/div/div/button"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[4]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/input"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[4]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/input"))).sendKeys("filebeat"+Keys.ARROW_DOWN+Keys.ENTER);
		//*[@id="discover-sidebar"]/div/discover-sidebar/section/div[1]/div/div/button/span/svg
		
		// Explore Metricbeat
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"discover-sidebar\"]/div/discover-sidebar/section/div[1]/div/div/button"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[4]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/input"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[4]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/input"))).sendKeys("metricbeat"+Keys.ARROW_DOWN+Keys.ENTER);
		//Explore airbusclients dump data
                wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"discover-sidebar\"]/div/discover-sidebar/section/div[1]/div/div/button"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[4]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/input"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[4]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/input"))).sendKeys("airbusclients"+Keys.ARROW_DOWN+Keys.ENTER);
		


		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"kibana-body\"]/div/header/div/div[1]/div[1]/button"))).click();
	    //driver.quit()
	}
	catch (Exception e) {
			System.out.println(e);
                        Assert.fail(e)
		}	

		
	}
	
	//CREATE THE AIRBUS INDEX
	@Test
	public void CreateIndexPattern() throws InterruptedException {
		try {
		driver.get(Kibana.Url);
		driver.manage().window().maximize();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"kibana-body\"]/div/header/div/div[1]/div[1]/button"))).click();
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Dashboard"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"kibana-body\"]/div/header/div/div[1]/div[1]/button"))).click();
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Stack Management"))).click();
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Index Patterns"))).click();
		//CREATE AIRBUS IndexPattern
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"kibana-body\"]/div/div[2]/div/div[2]/div/div/main/main/div/div[1]/div[2]/button"))).click();
	    
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("indexPattern")));
		
		System.out.println("ABLE TO FIND INDEX INPUT");
		Actions action = new Actions(driver); 
		WebElement element = driver.findElement(By.name("indexPattern"));
		element.click();
		element.clear();
		element.sendKeys("airbus");
        
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div/main/main/div[1]/div[2]/div[2]/div[2]/div/div/button/span"))).click();
		
		Thread.sleep(5000);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div/main/main/div[1]/div[2]/div[2]/div[2]/div/div/button/span"))).click();
	     
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"kibana-body\"]/div/div[2]/div/div[2]/div/div/main/main/div[1]/div[7]/div[2]/button/span"))).click();
	    driver.quit()
		}
		catch (Exception e) {
			System.out.println(e);
		}
		
		}
}
