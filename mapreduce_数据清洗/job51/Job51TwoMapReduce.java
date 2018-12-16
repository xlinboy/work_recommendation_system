package cn.hadoop.mapreduce.job51;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Job51TwoMapReduce {
	
	static class Job51TwoMapper extends Mapper<LongWritable, Text, Text, NullWritable> {
		Text k = new Text();
		NullWritable v = NullWritable.get();
		
		@Override
		protected void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {
			String line = value.toString();
			String[] fields = line.split("____");
			
			for (int i = 0; i < fields.length; i++) {
				fields[i] = fields[i].replaceAll(" ", "").replaceAll("\t", "");
			}
			if(fields.length < 7) return;
				
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
		job.setJarByClass(Job51TwoMapReduce.class);
		
		job.setMapperClass(Job51TwoMapper.class);
		
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(NullWritable.class);
		
		job.setReducerClass(job51TwoRedeucer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(NullWritable.class);
//		job.setNumReduceTasks(0);
		
		FileInputFormat.setInputPaths(job, new Path("C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\test_data\\input"));
		FileOutputFormat.setOutputPath(job, new Path("C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\test_data\\output1"));
		job.waitForCompletion(true);
	}
}
