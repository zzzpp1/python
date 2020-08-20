from Car import Car
'''
需求1构造一个停车场，停车场可以停车和取车，停车成功后得到停车票。 用户取车的时候也需要提供停车票，停车票有效，才可以成功取到车。
'''
class ParkingLot(Car):
    def __init__(self, capacity=2,park_name ='park'):
        # todo: 构造停车场所需的字段
        self.capacity = capacity             #停车场最大停车数
        self.name = park_name                 #停车场名字
        self.cars = []                        #车辆信息和停车票信息一致，停车证
        self.cur_car = len(self.cars)        #已停车数量
        self.ticket_mark = [0] * capacity    # 停车位停车情况
        self.car_to_carid=dict()             # 停车位和车辆信息对应情况

    def park_car(self, car: Car):
        # todo: 实现停车功能，成功停车后返回一个不重复的物体（object/uuid/……）作为停车票
        self.cur_car = len(self.cars)
        if self.cur_car>=self.capacity :
            print ("车库已满")
            return None
        for i in range(self.capacity):
            if self.ticket_mark[i] ==0:
                self.ticket_mark[i]=1
                self.car_to_carid[car] = i  # 将carid与停车票存储下来
                break
        self.cars.append(car)
        ticket=car.car_number
        print("车牌号为%s的车辆成功入库，停车位为%d" % (car.car_number,self.car_to_carid[car]))
        #print (self.cars)
        return ticket

    def take_car(self,ticket):
        flag=0
        for car in self.cars:
            if car.car_number == ticket:
                flag=1
            # todo: 实现通过车票取车的功能
                car_carid=self.car_to_carid[car]
                self.ticket_mark[car_carid]=0
                print("停车位为%d已空"%car_carid)
                self.cars.remove(car)
                self.car_to_carid.pop(car)
                print("车牌号为%s的车辆成功出库" % ticket)
                return car
        if flag==0:
            print("停车票错误" )
            return None
'''
需求2构造一个停车小弟（ParkingBoy），他能够将车顺序停放到多个停车场，并可以取出
'''
class parkingboy(ParkingLot):
    def __init__(self,parking_lot:ParkingLot,parklot_number=2):
        # todo: 构造停车场所需的字段
        self.car_to_parklot = dict()             #停车场和车辆对应表
        self.parklot_number = parklot_number          #停车场数量
        self.park_lots=[]      #停车场列表
        self.car_list=[]       #车辆停车清单
        for i in range(self.parklot_number):
            park="park%d" %i
            parklot=ParkingLot(park_name=park)
            self.park_lots.append(parklot)
        self.park_mark = [0] * parklot_number   #停车场停车情况

    def park_car(self, car:Car):
        # todo: 实现停车功能，成功停车后返回一个不重复的物体（object/uuid/……）作为停车票
        flag=0
        for park_lot in self.park_lots:
            park_lot.cur_car = len(park_lot.cars)
            if park_lot.capacity - park_lot.cur_car:
                flag=1
                print("停车场号%s"%park_lot)
                ticket = park_lot.park_car(car)
                self.car_list.append(car)
                self.car_to_parklot[car] = park_lot
                return ticket,park_lot
        if flag==0:
            print('所有停车场已停满，无法停车！')
            return None

    def take_car(self,ticket):
        flag = 0
        for car in self.car_list:
            if car.car_number == ticket:
                flag = 1
                park_lot=self.car_to_parklot[car]
                park_lot.take_car(ticket)
                self.car_list.remove(car)
        if flag==0:
            print("停车票错误" )
            return None

'''
需求3构造一个聪明的停车小弟（Smart Parking Boy），他能够将车停在空车位最多的那个停车场      
'''
class smart_parkingboy(parkingboy):

    def park_car(self, car:Car):
        # todo: 实现停车功能，成功停车后返回一个不重复的物体（object/uuid/……）作为停车票
        remainder = []
        for park_lot in self.park_lots:
            park_lot.cur_car = len(park_lot.cars)
            temp=park_lot.capacity - park_lot.cur_car
            if temp:
                remainder.append(temp)
        myindex = remainder.index(max(remainder))
        park_lot=self.park_lots[myindex]
        print("停车场号%s"%park_lot)
        ticket = park_lot.park_car(car)
        self.car_list.append(car)
        self.car_to_parklot[car] = park_lot
        return ticket,park_lot

    def take_car(self,ticket):
        flag = 0
        for car in self.car_list:
            if car.car_number == ticket:
                flag = 1
                park_lot=self.car_to_parklot[car]
                park_lot.take_car(ticket)
                self.car_list.remove(car)
        if flag==0:
            print("停车票错误" )
            return None

'''
需求4构造一个超级停车小弟（Super Parking Boy），他能够将车停在空置率最高的那个停车场
'''
class super_parkingboy(parkingboy):

    def park_car(self, car:Car):
        # todo: 实现停车功能，成功停车后返回一个不重复的物体（object/uuid/……）作为停车票
        remainder = []
        for park_lot in self.park_lots:
            park_lot.cur_car = len(park_lot.cars)
            temp=park_lot.capacity - park_lot.cur_car
            temp = temp / park_lot.capacity
            if temp:
                remainder.append(temp)
        myindex = remainder.index(max(remainder))
        park_lot=self.park_lots[myindex]
        print("停车场号%s"%park_lot)
        ticket = park_lot.park_car(car)
        self.car_list.append(car)
        self.car_to_parklot[car] = park_lot
        return ticket,park_lot

    def take_car(self,ticket):
        flag = 0
        for car in self.car_list:
            if car.car_number == ticket:
                flag = 1
                park_lot=self.car_to_parklot[car]
                park_lot.take_car(ticket)
                self.car_list.remove(car)
        if flag==0:
            print("停车票错误" )
            return None

'''
需求5构造停车场的经理（Parking Manager），他要管理多个停车仔，让他们停车，同时也可以自己停车
'''

class parkingmanager(parkingboy):

    def boy_park(self, car, boy,park_manner):
        if boy=='parkingboy':
            park_manner=parkingboy()
            park_manner.park_car(car)

        if boy=='smartparkingboy':
            park_manner=smart_parkingboy()
            park_manner.park_car(car)

        if boy=='superparkingboy':
            park_manner=super_parkingboy()
            park_manner.park_car(car)


if __name__ == "__main__":
    parking_lot = ParkingLot(2)
    while True:
        choice = input("请输入你要的功能:(1)存车；（2）取车:\n")
        if choice == '1':
            car_number = input("请输入车牌号:")
            car_owner = input("请输入车主姓名:")
            contact_way = input("请输入车主联系方式:")
            car_color = input("请输入车颜色:")
            car_model = input("请输入车型:")
            car = Car(car_number, car_owner, contact_way, car_color, car_model)
            ticket = parking_lot.park_car(car)
            print("取车证",ticket)
        if choice == '2':
            car_number = input("请输入车牌号:")
            ticket = car_number
            car=parking_lot.take_car(ticket)

