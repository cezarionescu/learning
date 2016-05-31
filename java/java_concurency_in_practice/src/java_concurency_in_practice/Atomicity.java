package java_concurency_in_practice;

import java.util.concurrent.atomic.AtomicLong;

public class Atomicity {
	private final AtomicLong count = new AtomicLong(0);
	public long getCount() {
		return count.get(); 
	}

	public void tick() {
		System.out.println("Tick = " + count.incrementAndGet());
	}
}
