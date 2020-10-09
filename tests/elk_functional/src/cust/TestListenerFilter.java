package cust;

import java.util.Set;

import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestNGMethod;
import org.testng.ITestResult;

public class TestListenerFilter implements ITestListener {

	    @Override
	    public void onTestStart(ITestResult result) {
	    }

	    @Override
	    public void onTestSuccess(ITestResult result) {
	    }

	    @Override
	    public void onTestFailure(ITestResult result) {
	    }

	    @Override
	    public void onTestSkipped(ITestResult result) {
	    }

	    @Override
	    public void onTestFailedButWithinSuccessPercentage(ITestResult result) {
	    }

	    @Override
	    public void onStart(ITestContext context) {
	    }

	    @Override
	    public void onFinish(ITestContext context) {
	        Set<ITestResult> failedTests = context.getFailedTests().getAllResults();
	        for (ITestResult temp : failedTests) {
	            ITestNGMethod method = temp.getMethod();
	            if (context.getFailedTests().getResults(method).size() > 1) {
	                failedTests.remove(temp);
	            } else {
	                if (context.getPassedTests().getResults(method).size() > 0) {
	                    failedTests.remove(temp);
	                }
	            }
	        }
	        Set<ITestResult>skippedTests = context.getSkippedTests().getAllResults();
	        for (ITestResult temps : skippedTests) {
	            ITestNGMethod method1 = temps.getMethod();
	            if (context.getSkippedTests().getResults(method1).size() > 1) {
	              skippedTests.remove(temps);
	            } else {
	                if (context.getPassedTests().getResults(method1).size() > 0) {
	                    skippedTests.remove(temps);
	                }
	            }
	        }
	    }
	
}
