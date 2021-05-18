import h5py

file_path = "/home/eiba_th/USERSTORE_eiba_th/exp_data/interactive_contact_class/memory_data/KROCO.hdf5"


def load_hdf5_dataset():
    # Test file content loading
    with h5py.File(file_path, "r") as f:
        print(f.keys())
        print(f['data'])
        print('\tFirst dataset:', f['data']['0'].__str__())
        print("\t\tattrs:", list(f['data']['0'].attrs.items()))
        print(f['labels'])


if __name__ == '__main__':
    load_hdf5_dataset()
