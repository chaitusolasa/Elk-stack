package elk_functionality;


import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import elk_functional_utilities.*;

public class DriverUtil {
	protected static WebDriver driver;
	protected WebDriverWait wd;
	JavascriptExecutor js = (JavascriptExecutor) driver;

	protected WebDriver getdriver() {
		if(driver==null) {
			System.setProperty("webdriver.chrome.driver",Kibana.Chromedriverpath);

			driver=new ChromeDriver();
		}
		return driver;
		
	}
}