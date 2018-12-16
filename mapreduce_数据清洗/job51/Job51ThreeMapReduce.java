package cn.hadoop.mapreduce.job51;

import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Reducer.Context;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import cn.hadoop.mapreduce.job51.Job51TwoMapReduce.job51TwoRedeucer;

public class Job51ThreeMapReduce {

	static class Job51ThreeMappper extends Mapper<LongWritable, Text, Text, NullWritable> {
		Text k = new Text();
		NullWritable v = NullWritable.get();

		@Override
		protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
			String line = value.toString();
			String[] fields = line.split("\t");		
			
			fields[1] = fields[1].split("-")[0];

			String exp = fields[2];
			if (exp.indexOf("无工作经验") != -1) {
				fields[2] = "0";
			} else if (exp.indexOf("年") != -1) {
				String age = exp.split("年")[0];
				fields[2] = age.split("-")[0];
			} else {
				fields[2] = "0";
			}

			String date = fields[5];

			if (date.indexOf("发布") != -1 ) {
				fields[5] = "2018-" + date.split("发")[0];
			} else {
				return;
			}

			String salary = fields[8];

			try {
				if (salary.indexOf("月") != -1) {
					fields[8] = Utils.salaryDeal(salary);
				} else if (salary.indexOf("年") != -1) {
					salary = Utils.salaryDeal(salary);
					fields[8] = String.valueOf((Float.parseFloat(salary) / 12));
				} else if (salary.indexOf("/天") != -1) {
					String range = salary.split("元")[0];
					float money = Float.parseFloat(range) * 22;
					fields[8] = String.valueOf(money);
				} else {
					System.out.println(salary);
					return;
				}
			} catch (Exception e) {
				System.out.println(e);
				System.out.println(fields[0] + "\t" + fields[1] + "\t" + salary);
			}

			StringBuffer sb = new StringBuffer();
			for (int i = 0; i < fields.length; i++) {
				sb.append(fields[i]);

				if (i == fields.length - 1)
					continue;
				sb.append("\t");
			}
						
			k.set(sb.toString());
			context.write(k, v);
		}

	}


	
	static class job51TwoRedeucer extends Reducer<Text, NullWritable, Text, NullWritable> {
		@Override
		protected void reduce(Text key, Iterable<NullWritable> value,
				Context context) throws IOException, InterruptedException {
			context.write(key, NullWritable.get());
		}
	}
	
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf);
		job.setJarByClass(Job51ThreeMapReduce.class);

		job.setMapperClass(Job51ThreeMappper.class);

		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(NullWritable.class);

//		job.setNumReduceTasks(0);
		job.setReducerClass(job51TwoRedeucer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(NullWritable.class);

		FileInputFormat.setInputPaths(job, new Path("C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\test_data\\output1"));
		FileOutputFormat.setOutputPath(job, new Path("C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\test_data\\output2"));
		job.waitForCompletion(true);
	}
}
