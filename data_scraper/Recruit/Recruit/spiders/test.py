import re
html = """<div class = "bmsg job_msg inbox" >
						<p > 销售主管/销售代表 < /p > <p > 岗位职责：< /p > <p > 1、负责制定区域市场营销计划，推动并帮助经销商制定市场营销计划；< /p > <p > 2、负责指导、协助经销商进行市场拓展及营销管理；< /p > <p > 3、负责销售市场信息的反馈收集并制订销售推广策略；< /p > <p > 4、负责销售渠道的开发、建设与维护，销售价格的控制与管理。< /p > <p > 任职要求：< /p > <p > 1、大专以上学历；< /p > <p > 2、有3年以上营销工作经历, 在市场拓展、开发、经销商管理有丰富的经验；< /p > <p > 3、良好的团队管理经验、思路清晰、有良好的市场规划能力、沟通谈判能力、良好的学习能力；< /p > <p > 4、熟悉终端精耕，有快速消费品、涂料、化工、建材行业工作经验者优先考虑；< /p > <p > 5、经验较少者可应聘销售代表岗位。< /p >
												<div class = "mt10" >
														<p class = "fp" >
								<span class="label">职能类别：</span>
																	<a class="el tdn" href="https://jobs.51job.com/putian/xiaoshouzhuguan/">
										销售主管									</a>
																		<a class="el tdn" href="https://jobs.51job.com/putian/xiaoshoudaibiao/">
										销售代表									</a>
																</p>
																					<p class="fp">
								<span class="label">关键字：</span>
																	<a class="el tdn" href="https://search.51job.com/list/110600,000000,0000,00,9,99,%25E5%25AE%25B6%25E8%25A3%2585,2,1.html?lang=c&amp;stype=1&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;lonlat=0%2C0&amp;radius=-1&amp;ord_field=0&amp;confirmdate=9&amp;fromType=&amp;dibiaoid=0&amp;address=&amp;line=&amp;specialarea=00&amp;from=&amp;welfare=">家装</a>
																	<a class="el tdn" href="https://search.51job.com/list/110600,000000,0000,00,9,99,%25E6%25B6%2582%25E6%2596%2599,2,1.html?lang=c&amp;stype=1&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;lonlat=0%2C0&amp;radius=-1&amp;ord_field=0&amp;confirmdate=9&amp;fromType=&amp;dibiaoid=0&amp;address=&amp;line=&amp;specialarea=00&amp;from=&amp;welfare=">涂料</a>
																	<a class="el tdn" href="https://search.51job.com/list/110600,000000,0000,00,9,99,%25E5%25BB%25BA%25E6%259D%2590,2,1.html?lang=c&amp;stype=1&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;lonlat=0%2C0&amp;radius=-1&amp;ord_field=0&amp;confirmdate=9&amp;fromType=&amp;dibiaoid=0&amp;address=&amp;line=&amp;specialarea=00&amp;from=&amp;welfare=">建材</a>
															</p>
													</div>						
						<div class="share">
							<a track-type="jobsButtonClick" event-type="6" class="a" href="javascript:void(0);" onclick="weixinMa();">微信分享</a>
															<div id="weixinMa_fx" style="display:none;"><img width="198" height="198" alt="二维码" src="https://jobs.51job.com/comm/qrcode.php?url=https%3A%2F%2Fm.51job.com%2Fsearch%2Fjobdetail.php%3Fjobid%3D111874159"></div>	
						</div>
						<div class="clear"></div>
					</div>"""
print(re.sub("\s|<.*?>", '', html))
