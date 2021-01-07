# Define global args
ARG LAYER_DIR="/opt/python"
ARG WORK_DIR="/opt/tmp"

FROM public.ecr.aws/lambda/python:3.8 as base-python38
RUN python3.8 -m pip install --upgrade pip


FROM base-python38 as build-image
ARG WORK_DIR
# Install dependencies
RUN yum install -y \
    freetype-devel \
    gcc \
    ghostscript \
    lcms2-devel \
    libffi-devel \
    libimagequant-devel \
    libjpeg-devel \
    libraqm-devel \
    libtiff-devel \
    libwebp-devel \
    make \
    openjpeg2-devel \
    rh-python36 \
    rh-python36-python-virtualenv \
    sudo \
    tcl-devel \
    tk-devel \
    tkinter \
    which \
    xorg-x11-server-Xvfb \
    zlib-devel \
    wheel \
    && yum clean all

RUN rm -rf /var/cache/yum
RUN mkdir -p ${WORK_DIR}

# Compile code with AVX2 flag
RUN export CC="cc -mavx2" 
RUN pip install --force-reinstall --no-cache-dir -t . --compile  pillow-simd -t ${WORK_DIR}

# RUN cp /usr/lib64/libtiff.so.5 ${LAYER_DIR}/libtiff.so.5
# RUN cp /usr/lib64/libjpeg.so.62 ${LAYER_DIR}/libjpeg.so.62
# RUN cp /usr/lib64/libjbig.so.2.0 ${LAYER_DIR}/libjbig.so.2.0
# RUN export LD_LIBRARY_PATH=${LAYER_DIR}


FROM build-image
ARG WORK_DIR
ARG LAYER_DIR
COPY --from=build-image ${WORK_DIR} ${LAYER_DIR}
COPY app.py requirements.txt ./
RUN python3.8 -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
