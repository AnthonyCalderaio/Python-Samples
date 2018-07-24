def main():
	my_dict = {
				'LB_58PLRL':(0.052 * 512506),
				'DET_HDGR':( 100 * 1),
				'INK_58SMARTIV PO':(0.075 * 100),
				'LB_58WARN':(0.045 * 10002),
				'INK_82EAGLEF':(0.44 * 100),
				'DET_DUAL':( 125 * 32),
				'LY_8':( 0.26 * 3),
				'BACK_NIP':(0.24 * 301),
				'T_58SUP3G PO':(0.37 * 2009),
				'LY_9':(0.26 * 512506),
				'P_FHG PO':( 0.05 * 1000),
				'T_58MINIPATRIOTPINB_2AL':(3.50 * 1000),
				'T_58MINIPATRIOTPINB_1AL':(0.45 * 101),
				'LB_58BCRLQ_1point7K':(0.06 * 1700),
				'LB_USP':(  0.062 * 5000),
				'DET_MAGNL':( 80 * 15),
				'INK_82EAGLE':( 0.42 * 1207),
				'T_82MINIB':( 0.15 * 100),
				'INK_58HAWKEYE':( 0.45 * 1002),
				'WRAP_B58G_2AL_36':( 3 * 1),
				'LB_58SEALS_NA WslashSEC DECT':(0.09 * 1101),
				'WRAP_MINIO58B_2AL_24':(6.75 * 3),
				'INK_58RNDBG_PO':( 0.075* 2000),
				'T_RFID223BS':(0.43 * 100),
				'LY_10DWPSUPB':(0.50 * 2),
				'T_58MILLI B WslashLY SWIVEL':( 0.21 * 100),
				'DET_SUPPRparenMK200parenPO':(325 * 11),
				'T_58SUPERMAX':( 0.10 * 65001),
				'INK_82SVR':(0.25 * 100)
				
				
}
	total = sum(my_dict.values())
	print(total)


	#for key, value in my_dict.items():
		#print key + "----$"+str(value) 

main()