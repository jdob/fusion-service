from delete_all import delete_all
from populate_categories import CategoryPopulator
from populate_partners import PartnerPopulator


if __name__ == '__main__':
    cp = CategoryPopulator()
    pp = PartnerPopulator()

    delete_all()
    cp.add_categories()
    pp.add_partners()
