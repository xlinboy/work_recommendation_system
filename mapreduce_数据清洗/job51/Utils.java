package cn.hadoop.mapreduce.job51;

public class Utils {
	
	public static String[] moveElement(int index,String value, String[] array) {
		String[] newArray = new String[array.length + 1];
		for (int i = 0; i < array.length; i++) {
			newArray[i] = array[i];
		}
		for (int i = newArray.length - 1; i > index; i--) {
			newArray[i] = newArray[i - 1];
		}
		newArray[index] = value;
		array = newArray;
		return array;
	}
	
	public static Boolean isHasEducation(String education) {
		if (education.indexOf("本科")==-1 && education.indexOf("大专")==-1 
				&& education.indexOf("中专") ==-1 && education.indexOf("高中")==-1
				&& education.indexOf("初中")==-1 && education.indexOf("研究生")==-1
				&& education.indexOf("博士")==-1 && education.indexOf("学历")==-1
				&& education.indexOf("中技 ")==-1 && education.indexOf("硕士 ") == -1)  {
			return false;
		}
		return true;
	}
	
	public static Boolean isHasLanguage(String language) {
		if(language.indexOf("日语")==-1 && language.indexOf("英语")==-1 && language.indexOf("普通话")==-1
				&& language.indexOf("汉语")==-1 && language.indexOf("法语")==-1 
				&& language.indexOf("阿拉伯语")==-1 && language.indexOf("粤语")==-1
				&& language.indexOf("韩语")==-1 )  {
			return false;
		}
		
		return true;
	}
	
	public static Boolean isCompany(String company) {
		if(company.indexOf("公司") == -1 && company.indexOf("商务") == -1
							&& company.indexOf("有限") == -1 && company.indexOf("研发中心") == -1
							&& company.indexOf("美团") == -1 && company.indexOf("科技") == -1
							&& company.indexOf("字节跳动") == -1 && company.indexOf("集团") == -1
							&& company.indexOf("服务" )== -1 && company.indexOf("中心") == -1
							&& company.indexOf("企业") == -1 && company.indexOf("股份") == -1
							&& company.indexOf("运营") == -1 && company.indexOf("研究") == -1
							&& company.indexOf("CHARLES") == -1 && company.indexOf("金色未来") == -1
							&& company.indexOf("北疆") == -1 && company.indexOf("屏幕") == -1
							&& company.indexOf("通迅") == -1 && company.indexOf("猫酷") == -1
							&& company.indexOf("Technologies") == -1 && company.indexOf("销售") == -1
							&& company.indexOf("石家庄")==-1 && company.indexOf("地产") == -1
							&& company.indexOf("总部")==-1 && company.indexOf("Adhub") == -1
							&& company.indexOf("东软睿博")==-1 && company.indexOf("小码联城") == -1
							&& company.indexOf("培训")==-1 && company.indexOf("播")==-1) {
			return false;
		}
		return true;
	}
	
	public static String salaryDeal(String salary) {
		if (salary.indexOf("万") != -1) {
			if( salary.indexOf("以下") != -1 ) {
				String range = salary.split("万")[0];
				float max = Math.round(Float.parseFloat(range) * 10000);
				salary = String.valueOf(max);
			} else if (salary.indexOf("以上") != -1) {
				String range = salary.split("万")[0];
				float min = Math.round(Float.parseFloat(range) * 10000);
				salary = String.valueOf(min);
			} else {
				String range = salary.split("万")[0];
				String[] split = range.split("-");
				float min = Math.round(Float.parseFloat(split[0]) * 10000);
				float max = Math.round(Float.parseFloat(split[1]) * 10000);
				salary =String.valueOf((max+min)/2);
			}
			
		} else if (salary.indexOf("千") != -1) {
			if( salary.indexOf("以下") != -1 ) {
				String range = salary.split("千")[0];
				float max = Float.parseFloat(range) * 1000;
				salary = String.valueOf(max);
			} else if (salary.indexOf("以上") != -1) {
				String range = salary.split("千")[0];
				float min = Float.parseFloat(range) * 1000;
				salary = String.valueOf(min);
			} else {
				String range = salary.split("千")[0];
				String[] split = range.split("-");
				float min = Float.parseFloat(split[0]) * 1000;
				float max = Float.parseFloat(split[1]) * 1000;
				salary = String.valueOf((max+min)/2);
			}
		}  
		return salary;
	}
}
 