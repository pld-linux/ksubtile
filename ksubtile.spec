# TODO
#  - Group? KDE-Group(s)?
Summary:	KSubtile, a SRT subtitle editor
Summary(pl):	KSubtile - edytor napisów SRT
Name:		ksubtile
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/ksubtile/%{name}-%(echo %{version} | tr _ -).tar.gz
# Source0-md5:	2fa967e96090a1f95fb747912c5c5100
URL:		http://ksubtile.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an editor for the KDE environment to edit, make and save
subtitles in the SRT subtitle format.

%description -l pl
Ten program jest edytorem dla ¶rodowiska KDE s³u¿±cym do
modyfikowania, tworzenia i zapisywania napisów w formacie SRT.

%prep
%setup -q -n %{name}-%(echo %{version} | cut -d_ -f1)

%{__sed} -i -e 's/Terminal=0/Terminal=false/' src/*.desktop
echo "Categories=Qt;KDE;Utility;" >> src/%{name}.desktop

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
#{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_desktopdir}/*
%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
