# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import pandas as pd

DM_FILEPATH =   "X:/AOS/master_files/aos/data_mart"
DM_ID =         "d430b4cd-ecb0-4a82-964f-ece5dd8544b7_aosdm.ippsa.test_"
ADDRESS_TAG =   "DmIppsaAddrTbl"
BILLET_TAG =    "DmIppsaBilletTbl"
OE_TAG =        "DmIppsaOeTbl"

class Increment:
    def __init__(self, inc_id, dm_id):        
        self._table_types = {
            "address" : False,
            "billet" : False,
            "oe" : False        
        }
        self._address_df = pd.read_excel(DM_FILEPATH + "/headers/dm_addr_hdr.xlsx")
        self._billet_df = pd.read_excel(DM_FILEPATH + "/headers/dm_blt_hdr.xlsx")
        self._oe_df = pd.read_excel(DM_FILEPATH + "/headers/dm_oe_hdr.xlsx")
        self.inc_id = inc_id
        self.dm_id = dm_id
        self._load_increment_from_file(self.inc_id, self.dm_id)
        
    def _load_increment_from_file(self, inc_id, dm_id):
        pad = "0" * (4 - len(str(inc_id)))
        inc_file = et.parse(
            DM_FILEPATH + "/" + DM_ID + pad + str(inc_id) + ".xml"
        )
        print("** Loading increment file:", DM_ID + pad + str(inc_id) + ".xml **")
        for i in range(0, len(inc_file.getroot())):
            if ADDRESS_TAG in inc_file.getroot()[i].tag:
                print(" - Processing address table")
                for row in inc_file.getroot()[i]:
                    self.add_address_row(row.attrib)
                
            if BILLET_TAG in inc_file.getroot()[i].tag:
                print(" - Processing billet table")
                for row in inc_file.getroot()[i]:
                    self.add_billet_row(row.attrib)
    
            if OE_TAG in inc_file.getroot()[i].tag:
                print(" - Processing OE table")
                for row in inc_file.getroot()[i]:
                    self.add_oe_row(row.attrib)

    def add_address_row(self, address_row):
        self._address_df = self._address_df.append(
            address_row, ignore_index = True
        )
        self._table_types["address"] = True
        
    def add_billet_row(self, billet_row):
        self._billet_df = self._billet_df.append(
            billet_row, ignore_index = True
        )  
        self._table_types["billet"] = True
    
    def add_oe_row(self, oe_row):
        self._oe_df = self._oe_df.append(
            oe_row, ignore_index = True
        )
        self._table_types["oe"] = True
        
    def get_table_types(self):
        return self._table_types
    def get_address_df(self):
        return self._address_df
    def get_billet_df(self):
        return self._billet_df
    def get_oe_df(self):
        return self._oe_df
    
    
    
    

def load_baseline():
    pass
    
def load_increment(inc_id, dm_id):
    pad = "0" * (4 - len(str(inc_id)))
    inc_file = et.parse(
        DM_FILEPATH + "/" + DM_ID + pad + str(inc_id) + ".xml"
    )
    increment = Increment()
    print("** Loading increment file:", DM_ID + pad + str(inc_id) + ".xml **")
    for i in range(0, len(inc_file.getroot())):
        if ADDRESS_TAG in inc_file.getroot()[i].tag:
            print(" - Processing address table")
            for row in inc_file.getroot()[i]:
                increment.add_address_row(row.attrib)
            
        if BILLET_TAG in inc_file.getroot()[i].tag:
            print(" - Processing billet table")

        if OE_TAG in inc_file.getroot()[i].tag:
            print(" - Processing OE table")
    return increment
