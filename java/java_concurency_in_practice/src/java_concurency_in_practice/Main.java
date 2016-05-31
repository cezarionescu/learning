package java_concurency_in_practice;

public class Main {
	static Atomicity at = new Atomicity();
	static Volatile v = new Volatile();
	
	public static void main(String[] args) {
//		Thread threads[] = new Thread[10];
//		for (int i = 0; i< 10; i++) {
//			threads[i] = new Thread(new CustomRunnable(i));
//			threads[i].start();
//		}
		
		for (int i = 0; i < 10; i++) {
			System.out.println("Thread " + i + ": starting");
			new VolatileThread(i).start();
		}
		Thread.yield();
		System.out.println(Thread.currentThread().getName() + ": sleep");
		v.sleep();
	}
	
	static class VolatileThread extends Thread {
		private int index;
		
		public VolatileThread(int index) {
			this.index = index;
		}
		
		public void run() {
			v.tryToSleep(index);
		}
	}
	
	static class CustomRunnable implements Runnable {
		private int index;
		
		public CustomRunnable(int index) {
			this.index = index;
		}
		
		@Override
		public void run() {
			System.out.print("Thread " + index + " ticked ");
			at.tick();
		}
	}
}
