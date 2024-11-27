import sqlite3

from tables.eight_speed import insertEightSpeedData, createEightSpeedTable
from tables.nine_speed import insertNineSpeedData, createNineSpeedTable
from tables.ten_speed import insertTenSpeedData, createTenSpeedTable
from tables.eleven_speed import insertElevenSpeedData, createElevenSpeedTable
from tables import distributor_table

createEightSpeedTable()
insertEightSpeedData()

createNineSpeedTable()
insertNineSpeedData()

createTenSpeedTable()
insertTenSpeedData()

createElevenSpeedTable()
insertElevenSpeedData()
