import nibabel as nib

# 替换为您的 NIFTI 文件的路径
nii_file_path = 'path_to_your_nii_file.nii'

# 加载 NIFTI 文件
nii_image = nib.load('ADNI_RESIZED/ADNI_002_S_0295_MR_MPR__GradWarp__B1_Correction_Br_20070219174038655_S21856_I40967.nii')

# 获取影像数据
image_data = nii_image.get_fdata()

# 获取并打印影像的维度
print("Dimensions of the NIFTI image:", image_data.shape)

