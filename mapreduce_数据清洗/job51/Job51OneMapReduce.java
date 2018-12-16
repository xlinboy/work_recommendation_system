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
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Job51OneMapReduce {

	static class Job51Mapper extends Mapper<LongWritable, Text, Text, NullWritable> {
		Text k = new Text();
		NullWritable v = NullWritable.get();

		@Override
		protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
			String line = value.toString();
			
			String[] fields = line.split("\t");
			for (int i = 0; i < fields.length; i++) {
				fields[i] = replaceSpecialStr(fields[i].replace(" ", ""));
			}
			if(fields.length < 7) return;
			
			
			if (!Utils.isHasEducation(fields[3])) {
				fields = Utils.moveElement(3, "-", fields);
			}
			
			if (!Utils.isHasLanguage(fields[6])) {
				fields = Utils.moveElement(6, "-", fields);
			} 

			StringBuffer sb = new StringBuffer();
			for (int i = 0; i < fields.length; i++) {
				sb.append(fields[i]);
				if (i == fields.length - 1)
					continue;
				if (i == 6) {
					if (!Utils.isCompany(fields[7])) {
						sb.append("/");
						continue;
					}
				}
				sb.append("\t");		
			}

			k.set(sb.toString());
			
			context.write(k, v);
		}

	}

	public static String replaceSpecialStr(String str) {
		String repl = "";
		if (str != null) {
			Pattern p = Pattern.compile("\\s*|\t|\r|\n");
			Matcher m = p.matcher(str);
			repl = m.replaceAll("");
		}
		return repl;
	}

	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf);
		job.setJarByClass(Job51OneMapReduce.class);

		job.setMapperClass(Job51Mapper.class);

		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(NullWritable.class);

		job.setNumReduceTasks(0);

		FileInputFormat.setInputPaths(job, new Path("C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\task_02\\data.txt"));
		FileOutputFormat.setOutputPath(job, new Path("C:\\Users\\13194\\Desktop\\资料\\bigdataexam\\task_02\\output"));
		job.waitForCompletion(true);
	}
}
