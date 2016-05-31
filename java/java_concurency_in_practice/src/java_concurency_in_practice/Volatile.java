package java_concurency_in_practice;

public class Volatile {
	volatile boolean asleep = false;
	
	public void sleep() {
		System.out.println("Went to sleep");
		asleep = true;
	}

	public void tryToSleep(int i)  {
		while (!asleep) {
			System.out.println("Thread " + i + ": counting sheeps...");
		}
		System.out.println("Thread " + i + ": sleeping");
	}
}
