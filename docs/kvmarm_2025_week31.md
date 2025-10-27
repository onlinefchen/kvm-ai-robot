# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 11:43:01

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 327
- **总 Thread 数**: 31
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 25 threads (198 邮件)
- **RFC**: 2 threads (116 邮件)
- **Bug Report**: 2 threads (6 邮件)
- **Selftest**: 1 threads (3 邮件)
- **GIT PULL**: 1 threads (4 邮件)

---

## 📌 PATCH

共 25 个 thread

---

### Thread 1: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd

**📧 邮件数**: 48 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 29 Jul 2025 15:54:31 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）支持 mmap() 操作的补丁系列，特别是针对 guest_memfd（来宾内存文件描述符）的支持。

1. **原始补丁内容**：
   本次补丁的核心是启用 KVM 对 guest_memfd 的 mmap() 支持，允许主机用户空间映射由 guest_memfd 支持的内存。这一功能旨在提升 KVM 的内存管理能力，尤其是在处理机密和非机密虚拟机时。

2. **之前讨论要点**：
   之前的讨论集中在如何实现 mmap() 支持的基础设施，以及如何确保其与现有的 KVM 功能兼容。补丁的设计考虑了安全性和性能，特别是通过消除主机内核对来宾内存的直接映射来增强安全性。

3. **本周的新讨论与进展**：
   本周的讨论主要围绕补丁的具体实现和测试。参与者确认了补丁的多个方面，包括对 x86 和 arm64 架构的支持，确保了 mmap() 操作的正确性和安全性。补丁中引入了新的测试用例，以验证 mmap() 功能的有效性。此外，针对不同虚拟机类型的支持进行了详细讨论，确保了补丁的兼容性和功能完整性。参与者们对补丁的各个部分进行了审查，并表示支持，部分补丁已获得“Reviewed-by”标记，显示出积极的反馈和认可。

总的来说，本次讨论推动了 KVM 对 guest_memfd 的 mmap() 支持的实现，标志着 KVM 在内存管理方面的一个重要进步。

#### 📝 邮件列表

1. **[07-29 15:54]** [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 15:54]** [PATCH v17 01/24] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GUEST_MEMFD
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[07-29 15:54]** [PATCH v17 02/24] KVM: x86: Have all vendor neutral sub-configs
 depend on KVM_X86, not just KVM
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-29 15:54]** [PATCH v17 03/24] KVM: x86: Select KVM_GENERIC_PRIVATE_MEM directly
 from KVM_SW_PROTECTED_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[07-29 15:54]** [PATCH v17 04/24] KVM: x86: Select TDX's KVM_GENERIC_xxx dependencies
 iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-29 15:54]** [PATCH v17 05/24] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_HAVE_KVM_ARCH_GMEM_POPULATE
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[07-29 15:54]** [PATCH v17 06/24] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[07-29 15:54]** [PATCH v17 07/24] KVM: Fix comments that refer to slots_lock
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[07-29 15:54]** [PATCH v17 08/24] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[07-29 15:54]** [PATCH v17 09/24] KVM: x86: Enable KVM_GUEST_MEMFD for all 64-bit builds
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[07-29 15:54]** [PATCH v17 10/24] KVM: guest_memfd: Add plumbing to host to map
 guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[07-29 15:54]** [PATCH v17 11/24] KVM: guest_memfd: Track guest_memfd mmap support in memslot
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[07-29 15:54]** [PATCH v17 12/24] KVM: x86/mmu: Rename .private_max_mapping_level()
 to .gmem_max_mapping_level()
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[07-29 15:54]** [PATCH v17 13/24] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[07-29 15:54]** [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order when
 recovering hugepages
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[07-29 15:54]** [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[07-29 15:54]** [PATCH v17 16/24] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[07-29 15:54]** [PATCH v17 17/24] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[07-29 15:54]** [PATCH v17 18/24] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[07-29 15:54]** [PATCH v17 19/24] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
 backed by guest_memfd
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[07-29 15:54]** [PATCH v17 20/24] KVM: arm64: Enable support for guest_memfd backed memory
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[07-29 15:54]** [PATCH v17 21/24] KVM: Allow and advertise support for host mmap() on
 guest_memfd files
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[07-29 15:54]** [PATCH v17 22/24] KVM: selftests: Do not use hardcoded page sizes in
 guest_memfd test
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[07-29 15:54]** [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[07-29 15:54]** [PATCH v17 24/24] KVM: selftests: Add guest_memfd testcase to
 fault-in on !mmap()'d memory
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[07-30 15:33]** Re: [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
27. **[07-30 15:36]** Re: [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
28. **[07-30 15:37]** Re: [PATCH v17 16/24] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
29. **[07-30 16:20]** Re: [PATCH v17 24/24] KVM: selftests: Add guest_memfd testcase to
 fault-in on !mmap()'d memory
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
30. **[07-30 19:04]** Re: [PATCH v17 22/24] KVM: selftests: Do not use hardcoded page sizes
 in guest_memfd test
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
31. **[07-30 19:39]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
32. **[07-30 05:57]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[07-30 16:51]** Re: [PATCH v17 24/24] KVM: selftests: Add guest_memfd testcase to
 fault-in on !mmap()'d memory
   - 发件人: Fuad Tabba <tabba@google.com>
34. **[07-30 14:34]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Ackerley Tng <ackerleytng@google.com>
35. **[07-30 15:44]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Ackerley Tng <ackerleytng@google.com>
36. **[07-31 15:49]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
37. **[07-31 09:59]** Re: [PATCH v17 13/24] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: David Hildenbrand <david@redhat.com>
38. **[07-31 10:01]** Re: [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: David Hildenbrand <david@redhat.com>
39. **[07-31 09:05]** Re: [PATCH v17 15/24] KVM: x86/mmu: Extend guest_memfd's max mapping
 level to shared mappings
   - 发件人: Fuad Tabba <tabba@google.com>
40. **[07-31 09:06]** Re: [PATCH v17 13/24] KVM: x86/mmu: Hoist guest_memfd max level/order
 helpers "up" in mmu.c
   - 发件人: Fuad Tabba <tabba@google.com>
41. **[07-31 10:06]** Re: [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: David Hildenbrand <david@redhat.com>
42. **[07-31 09:07]** Re: [PATCH v17 04/24] KVM: x86: Select TDX's KVM_GENERIC_xxx
 dependencies iff CONFIG_KVM_INTEL_TDX=y
   - 发件人: Fuad Tabba <tabba@google.com>
43. **[07-31 09:08]** Re: [PATCH v17 03/24] KVM: x86: Select KVM_GENERIC_PRIVATE_MEM
 directly from KVM_SW_PROTECTED_VM
   - 发件人: Fuad Tabba <tabba@google.com>
44. **[07-31 09:08]** Re: [PATCH v17 02/24] KVM: x86: Have all vendor neutral sub-configs
 depend on KVM_X86, not just KVM
   - 发件人: Fuad Tabba <tabba@google.com>
45. **[07-31 09:10]** Re: [PATCH v17 14/24] KVM: x86/mmu: Enforce guest_memfd's max order
 when recovering hugepages
   - 发件人: Fuad Tabba <tabba@google.com>
46. **[07-31 09:15]** Re: [PATCH v17 12/24] KVM: x86/mmu: Rename .private_max_mapping_level()
 to .gmem_max_mapping_level()
   - 发件人: Fuad Tabba <tabba@google.com>
47. **[07-31 10:29]** Re: [PATCH v17 12/24] KVM: x86/mmu: Rename
 .private_max_mapping_level() to .gmem_max_mapping_level()
   - 发件人: David Hildenbrand <david@redhat.com>
48. **[07-31 09:33]** Re: [PATCH v17 12/24] KVM: x86/mmu: Rename .private_max_mapping_level()
 to .gmem_max_mapping_level()
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 2: [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM

**📧 邮件数**: 39 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 28 Jul 2025 17:52:47 +0000

#### 🤖 AI 总结

本邮件列表讨论的主题是为 KVM（Kernel-based Virtual Machine）实现 ARM SMMUv3 驱动，特别是在受保护的虚拟机（pKVM）环境下的应用。

**原始 Patch/问题内容**：
本次讨论的补丁系列（PATCH v3 00/29）主要是为 KVM 实现 ARM SMMUv3 驱动，目的是通过 IOMMU（输入输出内存管理单元）实现 DMA 隔离，以保护虚拟机的内存安全。

**之前讨论要点**：
在历史讨论中，参与者们探讨了 SMMUv3 驱动的设计和实现细节，包括如何通过共享代码来减少重复，如何处理设备的使能和禁用，以及如何在 pKVM 环境中管理 IOMMU。讨论还涉及到如何在 hypervisor 和主机之间进行有效的内存映射和管理。

**本周新讨论、新进展或结论**：
本周的讨论集中在多个补丁的具体实现上，包括：
1. **命令队列的设置**：为 SMMUv3 驱动配置命令队列，并确保其在 hypervisor 地址空间中正确映射。
2. **设备的使能和禁用**：实现了用于使能和禁用设备的 hypercall，确保在 pKVM 环境下，主机无法访问虚拟机的内存。
3. **IOMMU 操作的注册**：通过 IOMMU ops 注册 SMMUv3 驱动，支持身份域的映射。
4. **流表的设置**：为 SMMUv3 驱动配置流表，并在需要时懒惰地填充二级流表。

参与者们还讨论了如何将 SMMUv3 驱动与现有的 IOMMU 子系统分开，以便更好地管理和维护代码。整体来看，补丁系列的目标是增强 pKVM 的安全性和性能，同时确保代码的可维护性和可扩展性。

#### 📝 邮件列表

1. **[07-28 17:52]** [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[07-28 17:52]** [PATCH v3 01/29] KVM: arm64: Add a new function to donate memory with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[07-28 17:52]** [PATCH v3 02/29] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[07-28 17:52]** [PATCH v3 03/29] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[07-28 17:52]** [PATCH v3 04/29] iommu/io-pgtable-arm: Split the page table driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[07-28 17:52]** [PATCH v3 05/29] iommu/io-pgtable-arm: Split initialization
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[07-28 17:52]** [PATCH v3 06/29] iommu/arm-smmu-v3: Move some definitions to a new
 common file
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[07-28 17:52]** [PATCH v3 07/29] iommu/arm-smmu-v3: Extract driver-specific bits from
 probe function
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[07-28 17:52]** [PATCH v3 08/29] iommu/arm-smmu-v3: Move some functions to arm-smmu-v3-common.c
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[07-28 17:52]** [PATCH v3 09/29] iommu/arm-smmu-v3: Move queue and table allocation
 to arm-smmu-v3-common.c
   - 发件人: Mostafa Saleh <smostafa@google.com>
11. **[07-28 17:52]** [PATCH v3 10/29] iommu/arm-smmu-v3: Move firmware probe to arm-smmu-v3-common
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[07-28 17:52]** [PATCH v3 11/29] iommu/arm-smmu-v3: Move IOMMU registration to arm-smmu-v3-common.c
   - 发件人: Mostafa Saleh <smostafa@google.com>
13. **[07-28 17:52]** [PATCH v3 12/29] iommu/arm-smmu-v3: Split cmdq code with hyp
   - 发件人: Mostafa Saleh <smostafa@google.com>
14. **[07-28 17:53]** [PATCH v3 13/29] iommu/arm-smmu-v3: Move TLB range invalidation into
 a macro
   - 发件人: Mostafa Saleh <smostafa@google.com>
15. **[07-28 17:53]** [PATCH v3 14/29] KVM: arm64: iommu: Introduce IOMMU driver infrastructure
   - 发件人: Mostafa Saleh <smostafa@google.com>
16. **[07-28 17:53]** [PATCH v3 15/29] KVM: arm64: iommu: Shadow host stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
17. **[07-28 17:53]** [PATCH v3 16/29] KVM: arm64: iommu: Add a memory pool
   - 发件人: Mostafa Saleh <smostafa@google.com>
18. **[07-28 17:53]** [PATCH v3 17/29] KVM: arm64: iommu: Add enable/disable hypercalls
   - 发件人: Mostafa Saleh <smostafa@google.com>
19. **[07-28 17:53]** [PATCH v3 18/29] iommu/arm-smmu-v3-kvm: Add SMMUv3 driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
20. **[07-28 17:53]** [PATCH v3 19/29] iommu/arm-smmu-v3-kvm: Initialize registers
   - 发件人: Mostafa Saleh <smostafa@google.com>
21. **[07-28 17:53]** [PATCH v3 20/29] iommu/arm-smmu-v3-kvm: Setup command queue
   - 发件人: Mostafa Saleh <smostafa@google.com>
22. **[07-28 17:53]** [PATCH v3 21/29] iommu/arm-smmu-v3-kvm: Setup stream table
   - 发件人: Mostafa Saleh <smostafa@google.com>
23. **[07-28 17:53]** [PATCH v3 22/29] iommu/arm-smmu-v3-kvm: Reset the device
   - 发件人: Mostafa Saleh <smostafa@google.com>
24. **[07-28 17:53]** [PATCH v3 23/29] iommu/arm-smmu-v3-kvm: Support io-pgtable
   - 发件人: Mostafa Saleh <smostafa@google.com>
25. **[07-28 17:53]** [PATCH v3 24/29] iommu/arm-smmu-v3-kvm: Shadow the CPU stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
26. **[07-28 17:53]** [PATCH v3 25/29] iommu/arm-smmu-v3-kvm: Add enable/disable device HVCs
   - 发件人: Mostafa Saleh <smostafa@google.com>
27. **[07-28 17:53]** [PATCH v3 26/29] iommu/arm-smmu-v3-kvm: Add host driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
28. **[07-28 17:53]** [PATCH v3 27/29] iommu/arm-smmu-v3-kvm: Pass a list of SMMU devices
 to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
29. **[07-28 17:53]** [PATCH v3 28/29] iommu/arm-smmu-v3-kvm: Allocate structures and reset device
   - 发件人: Mostafa Saleh <smostafa@google.com>
30. **[07-28 17:53]** [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
31. **[07-29 08:44]** Re: [PATCH v3 20/29] iommu/arm-smmu-v3-kvm: Setup command queue
   - 发件人: Krzysztof Kozlowski <krzk@kernel.org>
32. **[07-29 09:55]** Re: [PATCH v3 20/29] iommu/arm-smmu-v3-kvm: Setup command queue
   - 发件人: Mostafa Saleh <smostafa@google.com>
33. **[07-30 11:42]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
34. **[07-30 15:07]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
35. **[07-30 13:47]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
36. **[07-31 14:17]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
37. **[07-31 13:57]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
38. **[07-31 17:44]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
39. **[08-01 15:59]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 3: [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO

**📧 邮件数**: 20 | **👥 参与者**: 6 | **📅 开始时间**: Tue, 29 Jul 2025 12:33:35 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）的补丁系列，主题为“去掉 vm_dead，基于 vm_bugged 进行 -EIO 的处理”。该补丁的主要目的是在处理虚拟机状态时，避免使用 vm_dead 标记，以减少潜在的竞争条件和错误。

**原始补丁内容**：
补丁系列包括五个部分，主要修改了 KVM 中对虚拟机状态的管理，特别是如何处理虚拟机的错误状态。补丁建议在虚拟机出现故障时，仅基于 vm_bugged 来拒绝 ioctl 调用，而不是简单地依赖 vm_dead。

**历史讨论要点**：
之前的讨论主要集中在 vm_dead 的使用及其潜在的安全隐患。参与者指出，使用 vm_dead 可能会导致对虚拟机状态的错误判断，从而引发不必要的错误处理。

**本周新讨论及进展**：
本周的讨论中，Sean Christopherson 提出了具体的补丁实现，并逐步解释了每个补丁的目的和必要性。特别是他强调了 vm_dead 的去除如何能更好地处理虚拟机的错误状态，而不引入额外的复杂性。Rick Edgecombe 等人对补丁进行了评审，并提出了一些建议，确保在虚拟机终止后，相关的 ioctl 调用不会导致不一致的状态。此外，补丁还引入了新的子 ioctl KVM_TDX_TERMINATE_VM，以提高内存回收的效率。整体来看，讨论围绕如何更安全地管理 KVM 的虚拟机状态展开，旨在提升系统的稳定性和安全性。

#### 📝 邮件列表

1. **[07-29 12:33]** [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 12:33]** [PATCH 1/5] KVM: Never clear KVM_REQ_VM_DEAD from a vCPU's requests
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[07-29 12:33]** [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected pending
 S-EPT Violation
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-29 12:33]** [PATCH 3/5] KVM: Reject ioctls only if the VM is bugged, not simply
 marked dead
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[07-29 12:33]** [PATCH 4/5] KVM: selftests: Use for-loop to handle all successful SEV migrations
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-29 12:33]** [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[07-29 22:27]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
8. **[07-29 15:54]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[07-29 22:58]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
10. **[07-29 16:08]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[07-29 23:13]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
12. **[07-30 09:20]** Re: [PATCH 3/5] KVM: Reject ioctls only if the VM is bugged, not
 simply marked dead
   - 发件人: Chao Gao <chao.gao@intel.com>
13. **[07-30 10:07]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
14. **[07-30 13:45]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
15. **[07-30 13:55]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
16. **[07-30 14:04]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
17. **[07-30 12:59]** Re: [PATCH 2/5] KVM: TDX: Exit with MEMORY_FAULT on unexpected
 pending S-EPT Violation
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
18. **[08-01 16:56]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Adrian Hunter <adrian.hunter@intel.com>
19. **[08-01 09:44]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[08-03 20:41]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Adrian Hunter <adrian.hunter@intel.com>

---

### Thread 4: [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 13:00:05 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要集中在 pKVM（Protected KVM）虚拟机的初始化和句柄管理上。

1. **原始补丁内容**：补丁系列的目标是修改 pKVM 虚拟机的句柄分配时机，将句柄的创建从虚拟机首次运行时提前到主机初始化虚拟机时。这是为了确保在虚拟机的内存与主机 MMU 关联时，句柄已经可用，从而避免在句柄未创建时发生 MMU 失效通知的问题。

2. **之前讨论要点**：历史讨论中没有具体提到，但补丁的背景是为了修复当前在虚拟机初始化过程中存在的句柄管理问题，确保在虚拟机生命周期的早期阶段能够正确地分配和管理句柄。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现上，包括将句柄的分配过程拆分为两个阶段：一个用于预留句柄，另一个用于初始化虚拟机状态。此外，补丁还重构了相关的函数以提高代码的可读性和可维护性。参与者 Fuad Tabba 提出了多个补丁，逐步实现了这一目标，并在最后一封邮件中确认了补丁的最终实现细节。

总体而言，本周的讨论展示了对 pKVM 虚拟机句柄管理的系统性改进，为未来的开发奠定了基础。

#### 📝 邮件列表

1. **[07-29 13:00]** [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-29 13:00]** [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-29 13:00]** [PATCH v1 2/8] KVM: arm64: Rename 'host_kvm' to 'kvm' in pKVM host code
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[07-29 13:00]** [PATCH v1 3/8] KVM: arm64: Clarify comments to distinguish pKVM mode
 from protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[07-29 13:00]** [PATCH v1 4/8] KVM: arm64: Decouple hyp VM creation state from its handle
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-29 13:00]** [PATCH v1 5/8] KVM: arm64: Separate allocation and insertion of pKVM
 VM table entries
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-29 13:00]** [PATCH v1 6/8] KVM: arm64: Consolidate pKVM hypervisor VM
 initialization logic
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-29 13:00]** [PATCH v1 7/8] KVM: arm64: Introduce separate hypercalls for pKVM VM
 reservation and initialization
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-29 13:00]** [PATCH v1 8/8] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[08-03 14:10]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 5: [PATCH 0/2] Dump instructions on panic for pKVM/nvhe

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 17 Jul 2025 23:47:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 和 nvhe 的内核补丁，主要目的是在内核崩溃时转储故障指令。历史讨论中，Mostafa Saleh 提出了两个补丁：第一个补丁（PATCH 1/2）实现了在 nvhe 模式下崩溃时打印指令代码，第二个补丁（PATCH 2/2）则计划为 pKVM 添加类似功能。之前的讨论集中在补丁的实现细节和潜在的代码问题上。

在本周的新讨论中，Oliver Upton 对第一个补丁提出了建议，认为应避免在受保护模式下使用某些函数，并建议将相关功能移至 mmu.c 文件中。Kunwu Chan 对 Mostafa 的补丁提出了一些疑问，特别是关于 CONFIG_PROTECTED_NVHE_STACKTRACE 的配置问题。Mostafa 随后澄清了这一点，并确认补丁在不同配置下的测试结果，最终得到了 Kunwu 的认可和测试反馈。

综上所述，本周的讨论主要围绕补丁的实现细节和测试结果进行，参与者们对补丁的有效性进行了验证，并提出了改进建议。

#### 📝 邮件列表

1. **[07-17 23:47]** [PATCH 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[07-17 23:47]** [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[07-24 23:51]** [PATCH 0/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[07-24 23:51]** [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
5. **[07-24 23:51]** [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
6. **[07-29 08:57]** Re: [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-29 09:01]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table
 periodically
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-31 20:58]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>
9. **[07-31 14:05]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[08-01 16:00]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>

---

### Thread 6: [PATCH v8 0/7] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 19 Jul 2025 02:11:22 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中支持 FF-A 1.2 及 SEND_DIRECT2 ABI 的补丁集，共包含 7 个补丁。FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。补丁的主要目的是确保主机不会使用低于已与虚拟机监控器协商的 FF-A 版本，以避免兼容性问题。

在历史讨论中，Per Larsen 提出了多个补丁，包括将 FF-A 1.2 接口标记为不支持、屏蔽 FFA_FEATURE 调用的响应、提升支持的 FF-A 版本至 1.2 以及在主机处理程序中支持 FFA_MSG_SEND_DIRECT_REQ2。这些补丁为实现 FF-A 1.2 的消息接口做了准备。

在本周的新讨论中，Will Deacon 对多个补丁给予了认可（Acked-by），并提出了一些建议，例如在 ffa_call_supported() 函数中，当 FF-A 版本低于 1.2 时返回 false，以提高代码的清晰度。此外，他建议在标记不支持的补丁中添加相应的处理，以确保补丁系列的可追溯性和兼容性。整体来看，讨论进展顺利，补丁逐步获得认可。

#### 📝 邮件列表

1. **[07-19 02:11]** [PATCH v8 0/7] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-19 02:11]** [PATCH v8 4/7] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-19 02:11]** [PATCH v8 5/7] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[07-19 02:11]** [PATCH v8 6/7] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[07-19 02:11]** [PATCH v8 7/7] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[07-29 16:45]** Re: [PATCH v8 4/7] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Will Deacon <will@kernel.org>
7. **[07-29 16:46]** Re: [PATCH v8 5/7] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Will Deacon <will@kernel.org>
8. **[07-29 16:49]** Re: [PATCH v8 6/7] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>
9. **[07-29 16:54]** Re: [PATCH v8 7/7] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 7: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 10:57:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁系列（PATCH v3 0/6）。该补丁系列的主要内容是为 KVM 工具添加对嵌套虚拟化的支持，允许虚拟机在 EL2 环境中运行。

在历史讨论中，补丁的背景是 ARMv8.3 架构更新引入了嵌套虚拟化的支持，之前的版本（v2）已经进行了一些初步的修改和功能添加。

本周的新讨论中，Andre Przywara 提出了六个补丁，具体包括：
1. 更新内核头文件以支持新的 EL2 能力。
2. 添加命令行选项 `--nested`，允许 VCPU 在 EL2 启动。
3. 增加 VGIC 设备控制以设置维护 IRQ。
4. 添加计数器偏移控制，便于测试定时器子系统。
5. 支持 FEAT_E2H0，以便在不支持 VHE 的情况下启动旧版来宾。
6. 生成 HYP 定时器中断说明符，支持嵌套虚拟化时的中断处理。

Marc Zyngier 对补丁进行了审查并表示赞赏，认为其工作非常出色。整体来看，这些补丁为 ARM64 的嵌套虚拟化提供了重要的支持，增强了 KVM 工具的功能。

#### 📝 邮件列表

1. **[07-29 10:57]** [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[07-29 10:57]** [PATCH kvmtool v3 1/6] Sync kernel UAPI headers with v6.16
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[07-29 10:57]** [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[07-29 10:57]** [PATCH kvmtool v3 3/6] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[07-29 10:57]** [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[07-29 10:57]** [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[07-29 10:57]** [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
8. **[07-29 11:03]** Re: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 30 Jul 2025 21:15:03 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 规范的补丁集（PATCH v9 0/6）。FF-A 1.2 引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息有效载荷。该补丁集的主要目的是确保主机在与虚拟机监控器（hypervisor）协商后，不能使用低于已协商版本的 FF-A 版本。

在历史讨论中，补丁集经历了多次修改，主要集中在更新对 SMCCC 1.2 的支持，以简化需要接受多个参数的接口的实现。此外，补丁还更新了对 FF-A 1.2 中可选和不支持接口的列表。

本周的新讨论中，Per Larsen 提出了多个补丁，主要包括：
1. 修正主机版本降级尝试时的返回值，确保已协商的版本保持不变。
2. 更新 FF-A 初始化和主机处理程序以使用 SMCCC 1.2。
3. 标记 FFA_NOTIFICATION_* 调用和 FF-A 1.2 中的可选接口为不支持，以防止它们被错误地代理。
4. 遮蔽 FFA_FEATURE 调用的响应，以确保返回的最小缓冲区大小符合要求。
5. 将支持的 FF-A 版本提升至 1.2，以启用 1.2 特有的消息接口。

所有补丁均获得了 Will Deacon 的认可，显示出社区对这些改动的支持。

#### 📝 邮件列表

1. **[07-30 21:15]** [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-30 21:15]** [PATCH v9 1/6] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-30 21:15]** [PATCH v9 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[07-30 21:15]** [PATCH v9 3/6] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[07-30 21:15]** [PATCH v9 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[07-30 21:15]** [PATCH v9 5/6] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[07-30 21:15]** [PATCH v9 6/6] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 9: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 23 Jul 2025 11:46:52 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主题为“启用非 CoCo 虚拟机的 guest_memfd 支持的内存的主机用户空间映射”。该补丁旨在允许虚拟机监控器（VMM）如 Firecracker 完全使用 guest_memfd 作为内存后端，以支持多种 KVM 的新用例。

在历史讨论中，Fuad Tabba 提出了补丁的主要变更，包括简化 Kconfig 选择和依赖关系，并始终启用 KVM x86 和 arm64 的 guest_memfd 支持。Sean Christopherson 指出，当前 KVM 对于使用 guest_memfd 作为私有内存的虚拟机类型缺乏支持，导致在 x86 上出现问题。

本周的新讨论中，Fuad 确认了自测用例在 x86 和 arm64 上均已通过，并对 Sean 提出的发送 v17 补丁没有异议，表示支持。整体来看，讨论进展顺利，补丁的测试结果积极，下一步将继续推进补丁的发布。

#### 📝 邮件列表

1. **[07-23 11:46]** [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-23 11:47]** [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-24 15:15]** Re: [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-24 16:46]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Ackerley Tng <ackerleytng@google.com>
5. **[07-25 07:56]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-28 08:00]** Re: [PATCH v16 22/22] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-28 08:05]** Re: [PATCH v16 00/22] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 10: [PATCH v1 0/4] A couple of improvements for VMM to inject external
 abort to guest

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 21:20:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）的一系列补丁，旨在增强虚拟机监控器（VMM）向客户机注入外部中止（abort）的能力。

1. **原始补丁内容**：补丁集包括四个部分，主要功能是扩展 KVM_SET_VCPU_EVENTS API，使其支持注入外部指令中止（IABT）和允许用户空间在注入同步外部中止（SEA）时提供指令特定异常寄存器（ESR）值。

2. **历史讨论要点**：之前的讨论集中在如何通过 KVM_SET_VCPU_EVENTS API 处理外部中止的注入，特别是用户空间如何更方便地模拟异常条件。补丁中提到的 ABI（应用二进制接口）变化引发了对是否需要引入新版本结构体的讨论。

3. **本周的新讨论与进展**：本周的讨论主要围绕补丁的具体实现和测试展开。补丁中添加了对外部指令中止的支持，并允许用户空间提供 ESR 值。测试代码也进行了更新，以验证新功能的正确性。此外，文档也更新了相关 API 的使用说明，明确了如何在用户空间中处理外部中止的注入。

总体而言，这些补丁提升了 KVM 的功能，使其在处理外部中止时更加灵活和强大，同时也确保了用户空间能够更好地控制和模拟异常情况。

#### 📝 邮件列表

1. **[07-31 21:20]** [PATCH v1 0/4] A couple of improvements for VMM to inject external
 abort to guest
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-31 21:20]** [PATCH v1 1/4] KVM: arm64: Allow userspace to inject external
 instruction abort
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-31 21:20]** [PATCH v1 2/4] KVM: arm64: Allow userspace to supply ESR when
 injecting SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[07-31 21:20]** [PATCH v1 3/4] KVM: selftests: Test injecting external abort with ISS
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[07-31 21:20]** [PATCH v1 4/4] Documentation: kvm: update UAPI for injecting SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 11: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 19 Jul 2025 14:24:45 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构中处理 SEA（System Error Acknowledgment）的补丁。原始补丁（PATCH v2 1/6）旨在实现虚拟机退出到用户空间，以更优雅地处理 SEA，尤其是在缺乏 APEI（ACPI Platform Error Interface）支持的情况下。

在历史讨论中，参与者 Oliver Upton 和 Jiaqi Yan 交流了补丁的细节，Oliver 表示会在其补丁中加入相关内容，并询问是否应将其作为提交作者合并到 Jiaqi 的 v3 补丁系列中。Jiaqi 强调了与上游合作的重要性，以尽快确定提议的方法和用户空间 API（UAPI）。

在本周的新讨论中，Oliver 更新了进展，提到已发布 VNCR（Virtual Non-Cacheable Register）修复，并建议 Jiaqi 在即将发布的 kvmarm-6.17 或 -rc1 版本上重新基于其工作。Jiaqi 随后确认已基于 VNCR 修复发送了 v3 版本的补丁，并在当前的 kvmarm/next 上进行了更新。

总结而言，本次讨论围绕 KVM 在 ARM64 中处理 SEA 的补丁展开，历史讨论中强调了补丁的重要性和合作意图，而本周的进展则集中在补丁版本的更新和修复上。

#### 📝 邮件列表

1. **[07-19 14:24]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-25 15:54]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-29 14:28]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-31 14:06]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 12: [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 20:58:41 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）处理 ARM 架构下的同步外部中止（SEA）的问题，提出了一系列补丁以改善当前的处理机制。

1. **原始问题**：当主机的 APEI（高级平台错误接口）无法处理来宾的同步外部中止时，KVM 目前直接向 VCPU 注入异步 SError，导致来宾内核崩溃。尤其是在现代数据中心服务器中，来宾 VCPU 处理可恢复的未更正内存错误时，这种情况并不少见。

2. **之前讨论要点**：历史上，KVM 将 SEA 委托给 APEI 处理，但并非所有平台都支持这种处理方式。当前的解决方案是通过向用户空间提供 KVM_EXIT_ARM_SEA 事件，让用户空间参与 SEA 的处理，从而避免直接导致来宾崩溃。

3. **本周的新讨论与进展**：本周的讨论中，Jiaqi Yan 提出了三个补丁：
   - **补丁 1**：引入了 KVM_CAP_ARM_SEA_TO_USER 功能，允许用户空间在处理 SEA 时接收 KVM_EXIT_ARM_SEA 事件，并提供相关信息（如 ESR 值、故障虚拟和物理地址）。
   - **补丁 2**：增加了自测功能，验证 KVM 在 APEI 无法处理 SEA 时的行为，确保用户空间能够正确处理 KVM_EXIT_ARM_SEA。
   - **补丁 3**：更新了文档，详细说明了新用户空间可见的功能和 API，指导用户如何启用和处理 SEA。

这些补丁的实施将使 KVM 在处理内存错误时更加灵活，减少来宾系统崩溃的风险，同时提升用户对虚拟机内存错误的可控性。

#### 📝 邮件列表

1. **[07-31 20:58]** [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-31 20:58]** [PATCH v3 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-31 20:58]** [PATCH v3 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[07-31 20:58]** [PATCH v3 3/3] Documentation: kvm: new UAPI for handling SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 13: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs are supported

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 22:37:10 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vGIC v4 转发设置的问题。原始的补丁（patch）旨在修复一个由于在设置或取消 vGIC v4 转发时未检查直接 IRQ 支持而导致的内核崩溃问题。具体来说，补丁通过在相关函数中添加对 `vgic_supports_direct_irqs()` 的检查来解决这个问题。

在之前的讨论中，Raghavendra Rao Ananta 提出了这个补丁，并详细描述了崩溃的原因和相关的错误信息。Oliver Upton 对此表示感谢，并提出了一个建议，认为在进行 vLPI 注入之前，应该检查客户机是否具备 ITS（中断控制器）。

本周的讨论中，Oliver 提出了对补丁的修改建议，增加了对 vLPI 和 vSGI 支持的处理。Raghavendra 对此修改表示认可，并确认已进行测试。最终，Oliver 被授权重新提交这个修改后的补丁。

总结而言，本周的进展主要是对补丁的进一步完善和测试，确保在设置 vGIC v4 转发时能够正确处理直接 IRQ 的支持情况。

#### 📝 邮件列表

1. **[07-28 22:37]** [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs are supported
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[07-29 07:37]** Re: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs
 are supported
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-29 09:56]** Re: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs
 are supported
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[07-29 11:02]** Re: [PATCH] KVM: arm64: Set/unset vGIC v4 forwarding if direct IRQs
 are supported
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 14: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 11:23:42 -0700

#### 🤖 AI 总结

本邮件讨论主题为「[PATCH] KVM: arm64: nv: 处理由于 VNCR 重定向引起的 SEAs」，主要涉及对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的改进。

**原始 patch 内容**：
该补丁旨在处理通过 VNCR 页面重定向的系统寄存器访问可能引发的外部中止（SEAs）。补丁将这些中止路由到 `kvm_handle_guest_sea()` 函数，以便进行潜在的 APEI（ACPI 兼容的错误注入）处理，并在内核未处理的情况下回退到 vSError。

**之前讨论要点**：
在之前的讨论中，未提及具体的历史背景，但补丁的提出显然是为了改善对 VNCR 重定向引起的错误处理机制。

**本周的新讨论与进展**：
本周的讨论中，Oliver Upton 提交了补丁并指出了删除了一个不再需要的 `kvm_ras.h` 文件。Marc Zyngier 对补丁进行了审查并表示支持，随后提到将会发布一个单独的修复以解决补丁中未触发某些情况的问题。Oliver 对此表示感谢，并确认将采纳 Marc 的修复建议。整体来看，本周讨论积极，补丁得到了认可，并且后续修复工作也在进行中。

#### 📝 邮件列表

1. **[07-29 11:23]** [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-30 10:54]** Re: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-30 10:34]** Re: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 15: [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 23 Jul 2025 23:27:59 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下允许用户空间写入 GICD_TYPER2.nASSGIcap 的补丁（PATCH v5 0/6）。该补丁的主要目的是增强对虚拟化中中断控制器的支持，特别是在处理虚拟共享中断（vSGIs）和虚拟本地中断（vLPIs）时。

在历史讨论中，Oliver Upton 提出了该补丁的多个版本（v4 到 v5），并针对之前版本中的一些问题进行了修正，例如修正了 nASSGIreq 掩码的极性和避免了 irq_is_ppi() 的重复编码。此外，还增加了对 VGICv3 寄存器的文档描述，确保用户在初始化之前能够访问相关寄存器。

在本周的新讨论中，Eric Auger 对补丁进行了审核并表示支持，确认了补丁的有效性。Oliver Upton 随后宣布已将该补丁应用到下一个版本中，标志着这一功能的实现进入了下一阶段。补丁中的各个子项链接也被提供，以便于参与者查看具体的实现细节。

总体来看，本周的进展表明该补丁得到了积极的反馈并已成功整合，推动了 KVM 在 arm64 架构下的进一步发展。

#### 📝 邮件列表

1. **[07-23 23:27]** [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-28 18:07]** Re: [PATCH v5 0/6] KVM: arm64: Allow userspace to write
 GICD_TYPER2.nASSGIcap
   - 发件人: Eric Auger <eauger@redhat.com>
3. **[07-28 10:15]** Re: [PATCH v5 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 16: [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 08:26:03 -0700

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list”，主要讨论了在 KVM 的 arm64 自测试中添加 FEAT_RAS EL2 寄存器（VDISR_EL2 和 VSESR_EL2）到寄存器列表中，以便在嵌套虚拟机中对用户空间可见。

在本周的新讨论中，Oliver Upton 提出了该补丁，具体修改了 `get-reg-list.c` 文件，增加了对 VDISR_EL2 和 VSESR_EL2 寄存器的支持。Marc Zyngier 对该补丁表示认可（Acked-by），并确认了其有效性。最终，Oliver Upton 宣布该补丁已被应用到下一步开发中。

总结来看，本周的讨论主要集中在补丁的提出、认可及应用上，标志着对 KVM arm64 自测试功能的进一步完善。

#### 📝 邮件列表

1. **[07-28 08:26]** [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-28 16:47]** Re: [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-28 10:15]** Re: [PATCH] KVM: arm64: selftests: Add FEAT_RAS EL2 registers to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 17: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sat,  2 Aug 2025 18:40:21 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM（Kernel-based Virtual Machine）在 arm64 架构下的页面表转储（ptdump）中执行属性的打印问题。原始的补丁（patch）由 Wei-Lin Chang 提出，目的是修正当前在转储中可执行属性的显示错误，导致不可执行区域显示为 "X"，而可执行区域显示为空格。补丁通过交换这两个字符串来解决此问题。

在之前的讨论中，并没有提供具体的历史背景，但本周的讨论中，Wei-Lin Chang 提出了补丁的具体实现，并附上了代码修改的细节。Anshuman Khandual 对此补丁提出了质疑，指出 KVM_PTE_LEAF_ATTR_HI_S2_XN 宏的语义本身就是反向的，即当该宏被设置时，表示该条目不可执行，反之亦然。

本周的讨论主要集中在补丁的合理性和实现细节上，尚未达成最终结论。

#### 📝 邮件列表

1. **[08-02 18:40]** [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[08-03 19:33]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 11:18:28 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 VNCR_EL2 相关故障的补丁。原始补丁旨在修复对 ESR_EL2.VNCR 位的检查，确保在处理 VNCR_EL2 触发的故障时不会错误地测试 ESR_EL2.DFSC 中的随机位。Marc Zyngier 指出，之前的实现由于错误的位检查导致未能发现问题，因此建议将 BUG_ON() 改为 WARN_ON_ONCE()，以避免在此处崩溃。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测该补丁是基于对相关代码的审查而提出的，旨在提高故障处理的准确性。

本周的新进展包括 Marc Zyngier 提交的补丁和 Joey Gouly 的审查反馈，Joey 对补丁表示认可并给予了“已审查通过”的确认。这表明补丁得到了积极的响应，可能会在后续版本中合并。

#### 📝 邮件列表

1. **[07-30 11:18]** [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-31 11:07]** Re: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a
 VNCR_EL2 related fault
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 19: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 18 Jul 2025 14:45:17 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构上支持 FF-A（Firmware Framework for Arm）版本提升至 1.2 的补丁（PATCH v7 4/5）。

在历史讨论中，Per Larsen 提出了对该补丁的建议，认为应将其拆分为更小的部分，因为当前补丁涉及多个变更。他指出，检查 a2[15:2] 和 a3 位是不必要的，因为规范中规定这些位应为保留位（MBZ），未来若这些位被分配使用，当前的检查可能导致失败。此外，提升到 v1.2 的变更也可以单独处理。

在本周的新讨论中，Marc Zyngier 对之前的讨论进行了回应，表达了他对检查 MBZ 位的看法。他认为，如果不检查 v1.2 及之前版本中的这些位，未来若这些位被分配意义时，将无法正确理解其含义。因此，他主张在支持该版本之前，必须强制执行 MBZ 的检查，以避免错误的理解和处理。

总体来看，讨论围绕如何合理地处理 FF-A 版本提升的补丁展开，涉及补丁的拆分、检查必要性及未来兼容性等问题。

#### 📝 邮件列表

1. **[07-18 14:45]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>
2. **[07-31 08:56]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH v2] KVM: arm64: Move bundling vLPI and vSGI to vgic_supports_direct_msis()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 21:06:44 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及将 vLPI（虚拟本地中断）和 vSGI（虚拟共享中断）捆绑逻辑移动到 `vgic_supports_direct_msis()` 函数中。

在历史讨论中，补丁的背景是由于之前的提交（commit <c652887a9288>）在处理 vGIC v4 的初始化和拆解时，错误地忽略了 KVM 设置或取消 vGIC v4 转发的情况，导致内核出现空指针解引用的崩溃错误。

本周的新讨论中，Raghavendra Rao Ananta 提出了修复方案，建议将 vLPI 和 vSGI 的捆绑逻辑移动到 `vgic_supports_direct_msis()` 函数中，这样可以正确处理 vGIC v4 的初始化，同时也有助于 vLPI 的设置和取消转发。Oliver Upton 对此补丁进行了确认，并表示已将其应用于修复中。

总结来说，当前的讨论集中在修复 KVM arm64 中的一个潜在崩溃问题，并通过调整代码逻辑来确保系统的稳定性。

#### 📝 邮件列表

1. **[07-29 21:06]** [PATCH v2] KVM: arm64: Move bundling vLPI and vSGI to vgic_supports_direct_msis()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[07-29 14:23]** Re: [PATCH v2] KVM: arm64: Move bundling vLPI and vSGI to vgic_supports_direct_msis()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 18 Jul 2025 12:11:50 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 GICv3 系统寄存器访问问题的修复和测试。历史讨论中，Marc Zyngier 提出了一个补丁集，主要解决了一个导致用户空间无法访问 ICH_HCR_EL2 寄存器的错误。补丁的第一部分修复了系统寄存器表的顺序，确保 ICH_HCR_EL2 被正确放置。接下来的两个补丁则确保表格的排序检查与其他表格一致，最后一个补丁增强了 vgic_init 自测，确保可以访问这些寄存器。

在本周的新讨论中，Oliver Upton 表示已将该补丁集应用到下一个版本中，确认了补丁的有效性。补丁集包括四个部分，分别是修复 ICH_HCR_EL2 的排序、澄清重置回调的检查、强制 GICv3 系统寄存器表的排序，以及增加基本的 GICv3 系统寄存器用户空间访问测试。这标志着该问题的修复工作已得到认可并进入后续开发阶段。

#### 📝 邮件列表

1. **[07-18 12:11]** [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-28 10:15]** Re: [PATCH 0/4] KVM: arm64: Userspace GICv3 sysreg access fixes and testing
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 22: [PATCH v9 19/43] arm64: RME: Allow populating initial contents

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 18:56:38 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH v9 19/43），其目的是允许在内存管理中填充初始内容。该补丁的背景是为了支持通过 guest_memfd 使用 hugetlb 页面进行就地转换（in-place conversion），这是一个正在讨论中的特性。

在之前的讨论中，参与者提到在进行内存转换时，KVM 对由 guest_memfd 提供的 folios 的引用计数（refcounts）管理需要重新考虑，因为在内存转换过程中会对 folios 进行拆分和合并。讨论中提出了两种避免引用计数问题的策略：一是明确告知 guest_memfd 某个物理页框（pfn）正在被 KVM 使用，二是将该页标记为 hwpoisoned。

本周的新讨论中，Vishal Annapurve 提出了对上述策略的进一步疑问，询问是否假设了对来宾内存范围的双重备份，以及在 priv_pfn 和 pfn 相同的情况下，内存填充是否能与 CCA（Cache Coherent Architecture）正常工作。他对在支持就地转换的 guest_memfd 文件中，内存填充的具体实现表示好奇。这表明该补丁的实现细节仍需进一步探讨和验证。

#### 📝 邮件列表

1. **[07-31 18:56]** Re: [PATCH v9 19/43] arm64: RME: Allow populating initial contents
   - 发件人: Vishal Annapurve <vannapurve@google.com>

---

### Thread 23: [PATCH v3 05/15] KVM: x86: Add support for KVM userfault exits

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 30 Jul 2025 21:11:18 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 x86 架构上支持用户故障退出的补丁（PATCH v3 05/15）。该补丁旨在增强 KVM 的功能，允许在特定情况下处理用户故障。

在历史讨论中，虽然没有提供具体的上下文，但可以推测该补丁是为了改进 KVM 的内存管理和故障处理机制。补丁的主要内容涉及到在处理大页面时的错误处理逻辑。

在本周的新讨论中，参与者 James Houghton 指出该补丁未能移除 `recover_huge_pages_range()` 函数中的警告（WARN）。他提到，当启用 `KVM_MEM_LOG_DIRTY_PAGES` 和 `KVM_MEM_USERFAULT` 后，再禁用 `KVM_MEM_USERFAULT` 时会触发该警告。Houghton 还提到他与 Sean 进行了非公开讨论，正在等待 Sean 对 KVM_GENERIC_PAGE_FAULT 部分进行重构，并表示将投入更多时间关注 QEMU 相关的工作。

总体而言，本周的讨论集中在补丁的缺陷和后续改进计划上，显示出开发者对 KVM 功能增强的持续关注和合作。

#### 📝 邮件列表

1. **[07-30 21:11]** Re: [PATCH v3 05/15] KVM: x86: Add support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>

---

### Thread 24: [PATCH] Documentation: KVM: Use unordered list for pre-init VGIC registers

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Jul 2025 08:22:42 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 文档的一个补丁，旨在修正 VGIC（虚拟通用中断控制器）寄存器的文档格式问题。

1. **原始 patch/问题的内容**：补丁的目的是将原本试图创建的单列表格格式修正为无序列表，以解决文档构建时出现的错误。错误信息显示，使用的标记实际上是用于标题的，导致 Sphinx 文档构建失败。

2. **之前的讨论要点**：本邮件没有提供历史讨论的内容，表明该问题可能是首次被提出和讨论。

3. **本周的新讨论、进展或结论**：本周，Oliver Upton 提交了补丁，具体修改了 `arm-vgic-v3.rst` 文档，将原有的表格格式改为无序列表，修复了构建错误。补丁中指出了相关的寄存器字段，并提供了补丁的签名和报告者信息。此补丁已成功提交，解决了文档构建的问题。

#### 📝 邮件列表

1. **[07-29 08:22]** [PATCH] Documentation: KVM: Use unordered list for pre-init VGIC registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 25: [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 28 Jul 2025 14:07:36 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，目的是禁用 Clang 编译器中的一个警告——未初始化的常量指针警告。

**原始补丁内容**：
补丁由 Justin Stitt 提交，主要是为了处理 Clang 22 中出现的一个警告，指出在调用 `get_clidr_el1()` 函数时，传入的 `clidr` 变量是未初始化的常量指针。由于该函数并不关心指针的常量性，因此这是一个误报。补丁通过在 Makefile 中添加一行代码，强制禁用该警告，以避免浪费维护者的时间或在后续版本中引入大规模更改。

**之前讨论要点**：
在历史讨论中没有相关的补充内容，因此本次讨论主要集中在补丁本身的必要性和实现方式。

**本周的新讨论、进展或结论**：
本周的讨论主要围绕补丁的具体实现，Justin Stitt 提到该补丁不适用于 6.1 版本之后的代码，因为相关代码在后续的提交中已经被重构。此外，他还提到之前已为 5.15 版本发送了类似的补丁。整体来看，本周的讨论没有新的争议，补丁的必要性和实施方式得到了认可。

#### 📝 邮件列表

1. **[07-28 14:07]** [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning
   - 发件人: Justin Stitt <justinstitt@google.com>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v1 00/38] ARM CCA Device Assignment support

**📧 邮件数**: 115 | **👥 参与者**: 9 | **📅 开始时间**: Mon, 28 Jul 2025 19:21:37 +0530

#### 🤖 AI 总结

本邮件列表讨论的主题是关于 ARM CCA 设备分配支持的 RFC 补丁系列（v1 00/38）。以下是讨论的主要内容总结：

1. **原始补丁内容**：该补丁系列旨在实现 ARM CCA 架构中的设备分配支持，基于 Alp12 规范进行代码更改。补丁包括对 TSM 框架的扩展，使其在主机和来宾中均可使用。

2. **历史讨论要点**：之前的讨论集中在如何实现设备分配的工作流，包括主机和来宾之间的设备绑定和解绑定过程。补丁还涉及到与 RHI 接口的对接，确保设备在安全环境下的正确配置。

3. **本周的新讨论与进展**：
   - **新补丁**：补丁中增加了对 DMA 分配、设备通信、设备状态管理等功能的支持。
   - **接口报告和证书链的获取**：讨论中提到通过 RHI 调用从主机获取接口报告和证书链的支持。
   - **设备状态管理**：补丁中增加了对设备的启动和停止支持，确保设备在 TDISP 状态下的正确管理。
   - **退出处理程序**：增加了与设备分配相关的退出处理程序，以处理 REC 退出。
   - **代码审查和反馈**：参与者对补丁提出了多项建议，包括代码风格、错误处理和功能实现的清晰性。

整体来看，本周的讨论围绕着补丁的具体实现细节、潜在的设计问题以及如何确保设备在安全环境中的正确操作展开，参与者积极提供反馈和建议，以促进补丁的完善和最终合并。

#### 📝 邮件列表

1. **[07-28 19:21]** [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[07-28 19:21]** [RFC PATCH v1 01/38] tsm: Add tsm_bind/unbind helpers
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
3. **[07-28 19:21]** [RFC PATCH v1 02/38] tsm: Move tsm core outside the host directory
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
4. **[07-28 19:21]** [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
5. **[07-28 19:21]** [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private memory
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
6. **[07-28 19:21]** [RFC PATCH v1 05/38] tsm: Don't overload connect
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
7. **[07-28 19:21]** [RFC PATCH v1 06/38] iommufd: Add and option to request for bar mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
8. **[07-28 19:21]** [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate viommu with kvm instance
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
9. **[07-28 19:21]** [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
10. **[07-28 19:21]** [RFC PATCH v1 09/38] iommufd/vdevice: Add TSM Guest request uAPI
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
11. **[07-28 19:21]** [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
12. **[07-28 19:21]** [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
13. **[07-28 19:21]** [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform device driver
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
14. **[07-28 19:21]** [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
15. **[07-28 19:21]** [RFC PATCH v1 14/38] coco: host: arm64: Device communication support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
16. **[07-28 19:21]** [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the physical device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
17. **[07-28 19:21]** [RFC PATCH v1 16/38] X.509: Make certificate parser public
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
18. **[07-28 19:21]** [RFC PATCH v1 17/38] X.509: Parse Subject Alternative Name in certificates
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
19. **[07-28 19:21]** [RFC PATCH v1 18/38] X.509: Move certificate length retrieval into new helper
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
20. **[07-28 19:21]** [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
21. **[07-28 19:21]** [RFC PATCH v1 20/38] coco: host: arm64: Add support for creating a virtual device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
22. **[07-28 19:21]** [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual device communication
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
23. **[07-28 19:21]** [RFC PATCH v1 22/38] coco: host: arm64: Stop and destroy virtual device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
24. **[07-28 19:22]** [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest driver
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
25. **[07-28 19:22]** [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
26. **[07-28 19:22]** [RFC PATCH v1 25/38] cca: guest: arm64: Realm device lock support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
27. **[07-28 19:22]** [RFC PATCH v1 26/38] KVM: arm64: Add exit handler related to device assignment
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
28. **[07-28 19:22]** [RFC PATCH v1 27/38] coco: host: arm64: add RSI_RDEV_GET_INSTANCE_ID related exit handler
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
29. **[07-28 19:22]** [RFC PATCH v1 28/38] coco: host: arm64: Add support for device communication exit handler
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
30. **[07-28 19:22]** [RFC PATCH v1 29/38] coco: guest: arm64: Add support for collecting interface reports
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
31. **[07-28 19:22]** [RFC PATCH v1 30/38] coco: host: arm64: Add support for realm host interface (RHI)
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
32. **[07-28 19:22]** [RFC PATCH v1 31/38] coco: guest: arm64: Add support for fetching interface report and certificate chain from host
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
33. **[07-28 19:22]** [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest initiated TDI bind/unbind
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
34. **[07-28 19:22]** [RFC PATCH v1 33/38] KVM: arm64: CCA: handle dev mem map/unmap
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
35. **[07-28 19:22]** [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range found in the interface report
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
36. **[07-28 19:22]** [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start and stop support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
37. **[07-28 19:22]** [RFC PATCH v1 36/38] KVM: arm64: CCA: enable DA in realm create parameters
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
38. **[07-28 19:22]** [RFC PATCH v1 37/38] coco: guest: arm64: Add support for fetching device measurements
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
39. **[07-28 19:22]** [RFC PATCH v1 38/38] coco: guest: arm64: Add support for fetching device info
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
40. **[07-28 11:08]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
41. **[07-28 11:10]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
42. **[07-28 11:17]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
43. **[07-28 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
44. **[07-29 13:53]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
45. **[07-29 13:58]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
46. **[07-29 14:00]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
47. **[07-29 14:07]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
48. **[07-29 11:29]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
49. **[07-29 11:31]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
50. **[07-29 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
51. **[07-29 17:26]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
52. **[07-29 17:34]** Re: [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
53. **[07-29 18:10]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
54. **[07-29 18:22]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
55. **[07-29 20:16]** Re: [RFC PATCH v1 07/38] iommufd/viommu: Add support to associate
 viommu with kvm instance
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
56. **[07-29 20:19]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
57. **[07-29 20:22]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform device
 driver
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
58. **[07-30 14:43]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
59. **[07-30 14:55]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
60. **[07-30 14:12]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
61. **[07-30 14:28]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
62. **[07-30 11:09]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
63. **[07-30 11:25]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
64. **[07-30 11:28]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform
 device driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
65. **[07-30 11:38]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
66. **[07-30 13:23]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
67. **[07-30 13:39]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
68. **[07-30 15:07]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
69. **[07-30 14:52]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
70. **[07-30 14:57]** Re: [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the
 physical device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
71. **[07-30 15:08]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
72. **[07-30 15:12]** Re: [RFC PATCH v1 20/38] coco: host: arm64: Add support for
 creating a virtual device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
73. **[07-30 15:13]** Re: [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual
 device communication
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
74. **[07-30 15:15]** Re: [RFC PATCH v1 22/38] coco: host: arm64: Stop and destroy
 virtual device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
75. **[07-30 15:22]** Re: [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest
 driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
76. **[07-30 15:26]** Re: [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
77. **[07-30 15:32]** Re: [RFC PATCH v1 25/38] cca: guest: arm64: Realm device lock
 support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
78. **[07-30 15:35]** Re: [RFC PATCH v1 26/38] KVM: arm64: Add exit handler related to
 device assignment
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
79. **[07-30 15:43]** Re: [RFC PATCH v1 30/38] coco: host: arm64: Add support for realm
 host interface (RHI)
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
80. **[07-30 15:46]** Re: [RFC PATCH v1 31/38] coco: guest: arm64: Add support for
 fetching interface report and certificate chain from host
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
81. **[07-30 15:51]** Re: [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest
 initiated TDI bind/unbind
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
82. **[07-30 16:06]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
83. **[07-30 13:03]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
84. **[07-31 11:16]** Re: [RFC PATCH v1 37/38] coco: guest: arm64: Add support for
 fetching device measurements
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
85. **[07-31 11:36]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
86. **[07-31 11:40]** Re: [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start
 and stop support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
87. **[07-31 14:39]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
88. **[07-31 14:47]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
89. **[07-31 09:11]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
90. **[07-31 09:17]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
91. **[07-31 09:22]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
92. **[07-31 09:26]** Re: [RFC PATCH v1 12/38] coco: host: arm64: CCA host platform device
 driver
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
93. **[07-31 09:28]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
94. **[07-31 09:29]** Re: [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest
 driver
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
95. **[07-31 14:22]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
96. **[07-31 14:48]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
97. **[07-31 14:54]** Re: [RFC PATCH v1 23/38] coco: guest: arm64: Update arm CCA guest
 driver
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
98. **[07-31 13:44]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
99. **[07-31 13:46]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
100. **[07-31 13:53]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
101. **[07-31 19:07]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
102. **[08-01 10:31]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
103. **[08-01 10:30]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
104. **[08-01 11:53]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
105. **[08-01 12:51]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
106. **[08-01 14:19]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
107. **[08-01 17:54]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
108. **[08-02 14:14]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
109. **[08-02 14:33]** Re: [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
110. **[08-02 16:24]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
111. **[08-02 16:27]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
112. **[08-02 10:41]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
113. **[08-02 11:17]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
114. **[08-02 16:50]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
115. **[08-03 19:26]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 2: [RFC PATCH 06/34] KVM: gunyah: Add initial Gunyah backend
 support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 01 Aug 2025 13:25:43 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）中 Gunyah 后端支持的初步补丁（RFC PATCH 06/34）。该补丁旨在为 KVM 提供 Gunyah 虚拟化后端的支持，强调内核应提供一个通用的虚拟化 API，以适应不同的硬件和固件。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出参与者对补丁的初步构思表示认可，并认为内核的虚拟化能力应当独立于底层硬件。参与者提到，当前的实现中存在过多的条件编译指令（#ifdef），希望能够借鉴 x86 架构的静态调用模型，以减少代码复杂性。

在本周的新讨论中，David Woodhouse 对补丁表示支持，并提出了一些建议。他认为应当整合不同的虚拟化后端（如 Native KVM、pKVM、Gunyah 等），以实现一个统一的 KVM 用户空间 API。他建议开发一个灵活的模型，使得各个后端可以通过各自的实现插入基本的操作和钩子，从而减少对用户空间 API 的干扰。整体来看，本周的讨论集中在如何优化和整合虚拟化后端的实现，以提高代码的可维护性和一致性。

#### 📝 邮件列表

1. **[08-01 13:25]** Re: [RFC PATCH 06/34] KVM: gunyah: Add initial Gunyah backend
 support
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

## 📌 Bug Report

共 2 个 thread

---

### Thread 1: [Bug Report] external_aborts failure related to efa1368ba9f4 ("KVM:
 arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 21 Jul 2025 07:00:00 -0700

#### 🤖 AI 总结

本邮件线程讨论了与 KVM（Kernel-based Virtual Machine）相关的一个 bug 报告，具体是关于外部中断失败的问题，涉及到提交 efa1368ba9f4 的更改，该更改旨在立即提交 KVM_SET_VCPU_EVENTS 的异常。

在历史讨论中，Jiaqi Yan 提出了一个 bug 报告，指出在进行 SEA 注入开发时，运行 `external_aborts.c` 测试时出现失败，具体表现为测试断言失败，导致程序中断。Marc Zyngier 在后续邮件中建议检查一个特定的提交记录，以寻找可能的解决方案。

在本周的新讨论中，Jiaqi Yan 确认 Marc 提到的提交修复了他遇到的问题，表示感谢。这表明该问题已得到解决，相关的代码更改成功消除了外部中断失败的情况。整体来看，讨论围绕着一个具体的 bug 及其修复过程，最终达成了积极的结果。

#### 📝 邮件列表

1. **[07-21 07:00]** [Bug Report] external_aborts failure related to efa1368ba9f4 ("KVM:
 arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-25 15:38]** Re: [Bug Report] external_aborts failure related to efa1368ba9f4
 ("KVM: arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[07-26 10:18]** Re: [Bug Report] external_aborts failure related to efa1368ba9f4
 ("KVM: arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Marc Zyngier <maz@misterjones.org>
4. **[07-29 11:33]** Re: [Bug Report] external_aborts failure related to efa1368ba9f4
 ("KVM: arm64: Commit exceptions from KVM_SET_VCPU_EVENTS immediately")
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 2: [bug report] KVM: arm64: Add a range to __pkvm_host_unshare_guest()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Jul 2025 13:59:06 +0100

#### 🤖 AI 总结

在本次邮件讨论中，主要集中在 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个 bug 报告上。历史讨论中，Ben Horgan 提出了一个问题：在使用透明大页（transparent huge pages）启动 pkvm 客户机时，系统崩溃，错误信息显示在 `arch/arm64/kvm/hyp/nvhe/mem_protect.c` 文件的特定行。Ben 提供了一个补丁，修复了在 `__pkvm_host_relax_perms_guest()` 函数中对页面大小的错误假设，从而解决了崩溃问题。

在本周的新讨论中，Quentin Perret 对 Ben 的补丁表示认可，指出该补丁的思路是正确的，但同时也提到在另一个函数 `__pkvm_host_mkyoung_guest()` 中存在类似的问题，建议将其中的 PAGE_SIZE 替换为 0，以避免潜在的错误。Quentin 感谢 Ben 的报告，并表示将进一步关注这个问题。

总结来看，历史讨论中提出了一个关键的 bug 及其修复补丁，而本周的讨论则进一步确认了补丁的有效性，并指出了其他相关问题的修复建议。

#### 📝 邮件列表

1. **[07-22 13:59]** [bug report] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[07-28 15:38]** Re: [bug report] KVM: arm64: Add a range to
 __pkvm_host_unshare_guest()
   - 发件人: Quentin Perret <qperret@google.com>

---

## 📌 Selftest

共 1 个 thread

---

### Thread 1: KVM selftest for L2 guest execution fails

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 15:44:48 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测试中 L2 客户机执行失败的问题。Itaru Kitayama 提出了一个测试代码，该代码在 kvmarm/next 上运行时出现了错误，具体表现为 KVM_RUN 失败，返回错误代码 -1 和 errno 11（资源暂时不可用）。他请求社区的帮助以确定问题所在。

在之前的讨论中，Marc Zyngier 对 Itaru 的代码提出了批评，指出了多个设计上的问题，包括未正确配置 S2 转换、错误的 HCR_EL2 设置以及缺少 VNCR_EL2 的填充。他建议 Itaru 从一个简单的 L2 客户机开始，而不是直接使用复杂的 NV 功能，强调在实现 NV 之前，必须确保基础功能正常。

在本周的讨论中，Itaru 感谢了 Marc 的反馈，并表示将遵循他的建议进行修改。这表明他对解决问题持开放态度，并计划根据建议进行代码调整。整体来看，讨论集中在如何正确配置 KVM 的 L2 客户机以避免执行失败的问题上。

#### 📝 邮件列表

1. **[07-30 15:44]** KVM selftest for L2 guest execution fails  
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
2. **[07-30 13:24]** Re: KVM selftest for L2 guest execution fails  
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[07-31 06:40]** Re: KVM selftest for L2 guest execution fails  
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 changes for 6.17, round #1

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 11:17:35 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.17 版本中的首次更改，主要由 Oliver Upton 提交。此次提交的补丁包括了 GICv5 主机驱动的引入，这是针对 arm64 的下一代中断控制器，支持中断路由、MSI、中断翻译和有线中断等功能。此外，还包括对 GICv5 系统的虚拟化支持、用户空间对 GICv3 特性的控制、以及对嵌套支持的增强等。

在历史讨论中，未提及具体的背景信息，但本周的新讨论中，Oliver 提到这些更改是常规的更新，并强调了 GICv5 驱动的特殊性。Paolo Bonzini 对这些更改表示认可，并已将其合并。同时，Oliver 提出需要在文档中修复一个标记错误，以避免在 -next 版本中造成文档构建失败。

总结而言，本周的讨论主要集中在 KVM/arm64 的新特性和修复上，特别是 GICv5 驱动的集成及其对系统的影响，且已得到相关人员的认可和合并。

#### 📝 邮件列表

1. **[07-28 11:17]** [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-29 19:12]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[07-29 10:17]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-29 19:48]** Re: [GIT PULL] KVM/arm64 changes for 6.17, round #1
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

